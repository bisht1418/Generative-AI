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


if __name__ == '__main__':
    app.run()
