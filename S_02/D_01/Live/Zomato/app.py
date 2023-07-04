from flask import Flask, render_template, jsonify, request

# Create an instance of the Flask application
app = Flask(__name__)
app.debug = True

# Define a route and a corresponding view function

menu = [
    {'id': 1, 'name': 'Pizza', 'price': 10.99, 'availability': True},
    {'id': 2, 'name': 'Burger', 'price': 5.99, 'availability': True},
    {'id': 3, 'name': 'Pasta', 'price': 8.99, 'availability': False}
]

orders = []


@app.route('/')
def hello_world():
    message = "Hello, World!"
    return render_template('index.html', message=message)


@app.route('/menu', methods=['GET'])
def get_menu():
    return jsonify(menu)


@app.route('/menu', methods=['POST'])
def add_dish():
    new_dish = request.get_json()
    menu.append(new_dish)
    return jsonify(new_dish), 201


@app.route('/menu/<int:dish_id>', methods=['DELETE'])
def remove_dish(dish_id):
    for dish in menu:
        if dish['id'] == dish_id:
            menu.remove(dish)
            return jsonify({'message': 'Dish removed'})
    return jsonify({'message': 'Dish not found'}), 404


@app.route('/menu/<int:dish_id>', methods=['PATCH'])
def update_availability(dish_id):
    updated_dish = request.get_json()
    for dish in menu:
        if dish['id'] == dish_id:
            dish['availability'] = updated_dish['availability']
            return jsonify(dish)
    return jsonify({'message': 'Dish not found'}), 404


@app.route('/orders', methods=['POST'])
def take_order():
    order_data = request.get_json()
    customer_name = order_data.get('name')
    dish_ids = order_data.get('dish_ids')
    dish_quantity = order_data.get('dish_quantity')
    print(order_data, "id", dish_ids)
    if not customer_name or not dish_ids:
        return jsonify({'message': 'Invalid order data'}), 400

    order_items = []
    for dish_id in dish_ids:
        dish = next((dish for dish in menu if dish['id'] == dish_id), None)
        print(dish)
        if dish and dish['availability']:
            order_items.append({
                'id': dish_id,
                'name': dish['name'],
                'quantity': order_data["quantity"]
            })
        elif dish and not dish['availability']:
            return jsonify({'message': f"Dish '{dish['name']}' is not available"}), 400
        else:
            return jsonify({'message': f"Invalid dish ID '{dish_id}'"}), 400

    order = {
        'customer_name': customer_name,
        'order_items': order_items,
        'status': 'received',
        'order_id': len(orders) + 1
    }
    orders.append(order)
    return jsonify(order), 201


@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order_status(order_id):
    updated_status = request.get_json()['status']
    for order in orders:
        if order['order_id'] == order_id:
            order['status'] = updated_status
            return jsonify(order)
    return jsonify({'message': 'Order not found'}), 404


@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders)


@app.route('/exit', methods=['GET'])
def exit_application():
    # Perform any necessary cleanup or operations
    return jsonify({'message': 'Exiting the application'})


# Run the application
if __name__ == '__main__':
    app.run(use_reloader=True)
