from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

menu_items = []
orders = []


@app.route('/')
def index():
    return render_template('index.html', menu_items=menu_items, orders=orders)


@app.route('/menu', methods=['GET', 'POST', 'PUT', 'DELETE'])
def menu():
    if request.method == 'GET':
        return jsonify(menu_items)

    elif request.method == 'POST':
        new_item = {
            'id': request.form['id'],
            'name': request.form['name'],
            'price': request.form['price'],
            'availability': True
        }
        menu_items.append(new_item)
        return jsonify({'message': 'Menu item added successfully'})

    elif request.method == 'PUT':
        item_id = request.form['id']
        availability = request.form.get('availability', False)
        for item in menu_items:
            if item['id'] == item_id:
                item['availability'] = availability
                return jsonify({'message': 'Menu item availability updated successfully'})
        return jsonify({'error': 'Menu item not found'})

    elif request.method == 'DELETE':
        item_id = request.form['id']
        for item in menu_items:
            if item['id'] == item_id:
                menu_items.remove(item)
                return jsonify({'message': 'Menu item deleted successfully'})
        return jsonify({'error': 'Menu item not found'})


@app.route('/order', methods=['POST'])
def order():
    order_details = {
        'item_id': request.form['item_id'],
        'quantity': request.form['quantity'],
        'user_name': request.form['user_name']
    }
    orders.append(order_details)

    return jsonify({'message': 'Order placed successfully'})


if __name__ == '__main__':
    app.run(debug=True)
