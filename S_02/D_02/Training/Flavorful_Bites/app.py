from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.debug = True

# Define some sample data to simulate database records
menu = [
    {"dish_id": "1", "dish_name": "Pizza", "price": 10.99, "availability": "yes"},
    {"dish_id": "2", "dish_name": "Burger", "price": 5.99, "availability": "yes"},
    {"dish_id": "3", "dish_name": "Pasta", "price": 8.99, "availability": "yes"},
]
orders = []
order_id_counter = 1


@app.route('/')
def index():
    return render_template('index.html', menu=menu, orders=orders)


@app.route('/add_dish', methods=['POST'])
def add_dish():
    dish_name = request.form.get('dish_name')
    price = request.form.get('price')
    availability = request.form.get('availability')

    # Generate a unique dish ID (you can use a database-generated ID in a real application)
    dish_id = len(menu) + 1

    # Create a dictionary representing the new dish
    dish = {'dish_id': dish_id, 'dish_name': dish_name,
            'price': price, 'availability': availability}
    print(dish)
    # Add the dish to the menu
    menu.append(dish)

    return redirect('/')


@app.route('/update_availability', methods=['POST'])
def update_availability():
    dish_id = int(request.form.get('dish_id'))
    new_availability = request.form.get('new_availability')

    # Find the dish with the provided dish ID
    dish = next((d for d in menu if d['dish_id'] == dish_id), None)

    if dish:
        dish['availability'] = new_availability

    return redirect('/')


@app.route('/take_order', methods=['POST'])
def take_order():
    customer_name = request.form.get('customer_name')
    dish_ids = request.form.get('dish_ids')

    # Create a new order dictionary
    order = {'order_id': dish_ids, 'customer_name': customer_name,
             'dish_ids': dish_ids, 'status': 'received'}

    # Add the order to the list of orders
    orders.append(order)

    return redirect('/')


@app.route('/update_order_status', methods=['POST'])
def update_order_status():
    order_id = int(request.form.get('order_id'))
    new_status = request.form.get('new_status')

    # Find the order with the provided order ID
    order = next((o for o in orders if o['order_id'] == order_id), None)

    if order:
        order['status'] = new_status

    return redirect('/')


@app.route('/exit')
def exit():
    # Clear the menu and orders
    menu.clear()
    orders.clear()
    return "Thank you for using Zesty Zomato! Have a great day!"


if __name__ == '__main__':
    app.run(use_reloader=True)
