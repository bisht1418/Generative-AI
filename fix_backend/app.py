# from bson import ObjectId
from flask import jsonify
from pymongo import MongoClient
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from flask_marshmallow import Marshmallow
from bson.objectid import ObjectId
from mongoengine import Document, StringField, ReferenceField, DateTimeField, ObjectIdField, connect
from flask_cors import CORS

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb+srv://bishtnrj1418:neeraj@cluster0.ofkqsxc.mongodb.net/MovieMania?retryWrites=true&w=majority'
# Change this to a random secure key in production
app.config['JWT_SECRET_KEY'] = 'neeraj'
app.config['MONGODB_SETTINGS'] = {

    'host': 'mongodb+srv://bishtnrj1418:neeraj@cluster0.ofkqsxc.mongodb.net/MovieMania?retryWrites=true&w=majority'
}


# ====================================================
client = MongoClient(
    'mongodb+srv://bishtnrj1418:neeraj@cluster0.ofkqsxc.mongodb.net/MovieMania?retryWrites=true&w=majority')
db = client['MovieMania']
bookings_collection = db['bookings']
# ===================================================


CORS(app)

bcrypt = Bcrypt(app)
jwt = JWTManager(app)
ma = Marshmallow(app)

# Define a function to connect to MongoDB using the MONGODB_SETTINGS


def initialize_db(app):
    connect(host=app.config['MONGODB_SETTINGS']['host'])


initialize_db(app)

# Define data models for Users, Movies, Shows, Events, and Participants


class User(Document):
    username = StringField(required=True)
    email = StringField(required=True)
    password = StringField(required=True)
    role = StringField(default='regular')


class Movie(Document):
    Title = StringField(required=True)
    Year = StringField(required=True)
    imdbID = StringField(required=True)
    Type = StringField()
    Poster = StringField()
    _id = StringField()


class Show(Document):
    movie_id = ObjectIdField(required=True)
    show_time = StringField(required=True)
    category = StringField()


class Event(Document):
    name = StringField(required=True)
    description = StringField(required=True)
    event_date = StringField(required=True)
    venue = StringField(required=True)


class Participant(Document):
    user_id = ObjectIdField(required=True)
    event_id = ObjectIdField(required=True)


# Define a Marshmallow schema for the User data model
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'email', 'role')


# =============================================================


@app.route('/register', methods=['POST'])
def register():
    data = request.json
    existing_user = User.objects(email=data['email']).first()
    if existing_user:
        return jsonify({'message': 'User with this email already exists'}), 409

    hashed_password = bcrypt.generate_password_hash(
        data['password']).decode('utf-8')
    new_user = User(
        username=data['username'], email=data['email'], password=hashed_password)
    new_user.save()

    # Convert new_user to a dictionary before returning as a JSON response
    user_data = new_user.to_mongo().to_dict()

    # Convert ObjectId to string
    user_data['_id'] = str(user_data['_id'])

    return jsonify(message="successfully register", user=user_data)


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.objects(email=data['email']).first()
    if not user or not bcrypt.check_password_hash(user.password, data['password']):
        return jsonify({'message': 'Invalid email or password'}), 401

    # Convert ObjectId to string before returning the JSON response
    user_dict = user.to_mongo()
    user_dict['_id'] = str(user_dict['_id'])

    access_token = create_access_token(identity=str(user.id))
    return jsonify(user=user_dict, access_token=access_token)


@app.route('/users', methods=['GET'])
def get_users():
    users = User.objects().all()

    # Convert users to a list of dictionaries before returning as a JSON response
    users_data = [user.to_mongo().to_dict() for user in users]

    # Convert ObjectId to string for each user
    for user_data in users_data:
        user_data['_id'] = str(user_data['_id'])

    return jsonify(users=users_data)


@app.route('/movies', methods=['GET'])
def movies():
    if request.method == 'GET':
        movies = Movie.objects().all()
        movies_list = []
        for movie in movies:
            movie_dict = {
                'id': str(movie._id),
                'Title': movie.Title,
                "imdbID": movie.imdbID,
                'Year': movie.Year,
                'Poster': movie.Poster,
                "Type": movie.Type
            }
            movies_list.append(movie_dict)
        return jsonify(movies_list), 200


@app.route('/movies/<string:movie_id>', methods=['GET'])
def get_movie_by_id(movie_id):
    if request.method == 'GET':
        try:
            movie_id_obj = ObjectId(movie_id)
            movie = Movie.objects.get(_id=movie_id_obj)
            movie_data = {
                'id': str(movie._id),
                'Title': movie.Title,
                "imdbID": movie.imdbID,
                'Year': movie.Year,
                'Poster': movie.Poster,
                "Type": movie.Type
            }
            return jsonify(movie_data), 200
        except Movie.DoesNotExist:
            return jsonify({'message': 'Movie not found'}), 404


@app.route('/book', methods=['POST'])
def book_show():
    data = request.json
    bookings_collection.insert_one(data)

    return jsonify({'message': 'Booking successful!'}), 201


@app.route('/book', methods=['GET'])
def get_bookings():
    # Exclude the '_id' field from the results
    bookings = list(bookings_collection.find({}, {'_id': 0}))
    return jsonify(bookings), 200


if __name__ == '__main__':
    app.run(debug=True)
