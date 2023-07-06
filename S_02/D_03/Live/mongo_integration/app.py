from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)
client = MongoClient(
    'mongodb+srv://bishtnrj1418:neeraj@cluster0.xcumqmz.mongodb.net/zesty_zomato?retryWrites=true&w=majority')
db = client['zesty_zomato']


@app.route('/', methods=['GET'])
def index():
    return "Welcome to the database"


@app.route('/dishes', methods=['GET'])
def get_dishes():
    dishes = list(db.dishes.find())
    for dish in dishes:
        dish['_id'] = str(dish['_id'])  # Convert ObjectId to string
    return jsonify(dishes)


@app.route('/dishes', methods=['POST'])
def add_dish():
    dish = request.get_json()
    db.dishes.insert_one(dish)
    return jsonify({'message': 'Dish added successfully'})


# Order a menu
@app.route('/orders', methods=['POST'])
def order_menu():
    data = request.get_json()
    customer_name = data.get('customer_name')
    menu_id = data.get('_id')
    quantity = data.get('quantity')

    print(data, menu_id)

    if not customer_name or not menu_id or not quantity:
        return jsonify({'error': 'Incomplete order details'}), 400

    total_price = data.get('price') * quantity

    # Create the order document
    order = {
        'customer_name': customer_name,
        'menu_id': menu_id,
        'quantity': quantity,
        'total_price': total_price,
        "status": "received"
    }

    # Insert the order into the database
    result = db.orders.insert_one(order)
    order['_id'] = str(result.inserted_id)

    return jsonify(order), 201

# Retrieve all orders


@app.route('/orders', methods=['GET'])
def get_orders():
    orders = list(db.orders.find())
    for order in orders:
        order['_id'] = str(order['_id'])  # Convert ObjectId to string
    return jsonify(orders)


# Update dish availability
@app.route('/dishes/<dish_id>', methods=['PUT'])
def update_dish_availability(dish_id):
    print(dish_id)
    print(ObjectId)
    if not ObjectId.is_valid(dish_id):
        return jsonify({'error': 'Invalid dish ID'}), 400

    data = request.get_json()
    new_availability = data.get('availability')

    if new_availability is None:
        return jsonify({'error': 'Availability field is required'}), 400

    result = db.dishes.update_one({'_id': ObjectId(dish_id)}, {
                                  '$set': {'availability': new_availability}})

    if result.matched_count == 0:
        return jsonify({'error': 'Dish not found'}), 404

    return jsonify({'message': 'Dish availability updated successfully'})


if __name__ == '__main__':
    app.run()
