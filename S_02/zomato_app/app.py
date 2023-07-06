# app.py

from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin,current_user
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# MongoDB connection
client = MongoClient(
    'mongodb+srv://bishtnrj1418:neeraj@cluster0.xcumqmz.mongodb.net/zomato_db?retryWrites=true&w=majority')
db = client['zomato_db']

# Flask-Login configuration
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'admin_login'


# User model for Flask-Login
class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id

    def check_password(self, password):
        # Implement this method to validate the user's password
        user = db.users.find_one({'_id': ObjectId(self.id)})
        return user['password'] == password


@login_manager.user_loader
def load_user(user_id):
    return User(user_id)


# Admin routes and views
@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        print(username, password)

        user = db.admins.find_one({'username': username})
        if user and user['password'] == password:
            login_user(User(str(user['_id'])))
            return redirect(url_for('admin_dashboard'))
        else:
            flash('Invalid username or password', 'error')


    return render_template('admin_login.html')

# Admin Register
@app.route('/admin/register', methods=['GET', 'POST'])
def admin_register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            flash('Passwords do not match', 'error')
        else:
            existing_user = db.admins.find_one({'username': username})
            if existing_user:
                flash('Username already exists', 'error')
            else:
                user = {'username': username, 'password': password}
                db.admins.insert_one(user)
                flash('Registration successful. Please log in.', 'success')
                return redirect(url_for('admin_login'))

    return render_template('admin_register.html')


@app.route('/admin/logout')
@login_required
def admin_logout():
    logout_user()
    return redirect(url_for('admin_login'))


@app.route('/admin/dashboard')
@login_required
def admin_dashboard():
    food_items = db.food_items.find()
    return render_template('admin_dashboard.html', food_items=food_items)


@app.route('/admin/food_items/add', methods=['GET', 'POST'])
def admin_add_food_item():
    if request.method == 'POST':
        dish_name = request.form['dish_name']
        price = float(request.form['price'])
        availability = request.form.get('availability') == 'on'

        food_item = {
            'dish_name': dish_name,
            'price': price,
            'availability': availability
        }
        db.food_items.insert_one(food_item)

        return redirect(url_for('admin_dashboard'))

    return render_template('admin_add_food_item.html')


# User routes and views
@app.route('/')
def user_home():
    food_items = db.food_items.find({'availability': True})
    return render_template('user_home.html', food_items=food_items)


@app.route('/menu')
def user_menu():
    food_items = db.food_items.find({'availability': True})
    return render_template('user_menu.html', food_items=food_items)


@app.route('/place_order', methods=['POST'])
def place_order():
    dish_id = request.form['dish_id']
    quantity = int(request.form['quantity'])
    user_name = request.form['user_name']
    address = request.form['address']
    phone = request.form['phone']

    food_item = db.food_items.find_one({'_id': ObjectId(dish_id)})
    if food_item:
        total_price = food_item['price'] * quantity

        order = {
            'dish_id': dish_id,
            'quantity': quantity,
            'user_name': user_name,
            'address': address,
            'phone': phone,
            'status': 'Placed',
            'total_price': total_price
        }
        db.orders.insert_one(order)

        return redirect(url_for('user_orders'))

    return render_template('place_order.html')


@app.route('/orders')
def user_orders():
    orders = db.orders.find()
    return render_template('user_orders.html', orders=orders)


if __name__ == '__main__':
    app.run(debug=True)
