import json
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Menu data
menu = [
    {"dish_id": "1", "dish_name": "Pizza", "price": 10.99, "availability": "yes"},
    {"dish_id": "2", "dish_name": "Burger", "price": 5.99, "availability": "yes"},
    {"dish_id": "3", "dish_name": "Pasta", "price": 8.99, "availability": "yes"},
]

# Order data
orders = []

# Routes


@app.route('/', methods=['GET'])
def start_routes():
    return "welcome to flask backend"


@app.route('/menu', methods=['GET'])
def get_menu():
    return jsonify(menu)


@app.route('/menu', methods=['POST'])
def add_dish():
    dish = request.get_json()
    menu.append(dish)
    return jsonify({'message': 'Dish added successfully'})


@app.route('/menu/<dish_id>', methods=['DELETE'])
def remove_dish(dish_id):
    for dish in menu:
        if dish['id'] == dish_id:
            menu.remove(dish)
            return jsonify({'message': 'Dish removed successfully'})
    return jsonify({'message': 'Dish not found'})


@app.route('/menu/<dish_id>', methods=['PUT'])
def update_availability(dish_id):
    availability = request.get_json()['availability']
    for dish in menu:
        if dish['id'] == dish_id:
            dish['availability'] = availability
            return jsonify({'message': 'Availability updated successfully'})
    return jsonify({'message': 'Dish not found'})


@app.route('/orders', methods=['POST'])
def place_order():
    order = request.get_json()

    order['status'] = 'received'
    orders.append(order)
    return jsonify({'message': 'Order placed successfully', 'order_id': order})


@app.route('/orders/<order_id>', methods=['PUT'])
def update_order_status(order_id):
    status = request.get_json()['status']
    for order in orders:
        if order['id'] == order_id:
            order['status'] = status
            return jsonify({'message': 'Order status updated successfully'})
    return jsonify({'message': 'Order not found'})


@app.route('/orders', methods=['GET'])
def get_orders():
    status = request.args.get('status')
    if status:
        filtered_orders = [
            order for order in orders if order['status'] == status]
        return jsonify(filtered_orders)
    return jsonify(orders)

# Price Calculation route


@app.route('/orders/<order_id>/price', methods=['GET'])
def calculate_order_price(order_id):
    order = next((order for order in orders if order['id'] == order_id), None)
    if not order:
        return jsonify({'message': 'Order not found'})
    return jsonify({'total_price': order['total_price']})

# Status Filter route


@app.route('/orders/filter', methods=['GET'])
def filter_orders_by_status():
    status = request.args.get('status')
    if not status:
        return jsonify({'message': 'Status parameter is missing'}), 400
    filtered_orders = [order for order in orders if order['status'] == status]
    return jsonify(filtered_orders)

# Data Persistence


def save_data():
    with open('menu.json', 'w') as menu_file:
        json.dump(menu, menu_file)
    with open('orders.json', 'w') as orders_file:
        json.dump(orders, orders_file)


def load_data():
    global menu, orders
    try:
        with open('menu.json', 'r') as menu_file:
            menu = json.load(menu_file)
        with open('orders.json', 'r') as orders_file:
            orders = json.load(orders_file)
    except FileNotFoundError:
        menu = []
        orders = []


# Other routes and functionality can be added as needed
if __name__ == '__main__':
    app.run()
