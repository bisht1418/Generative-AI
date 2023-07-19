from bson import ObjectId
from flask import jsonify
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from flask_marshmallow import Marshmallow
from bson.objectid import ObjectId
from mongoengine import Document, StringField, ReferenceField, DateTimeField, ObjectIdField, connect


app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb+srv://bishtnrj1418:neeraj@cluster0.ofkqsxc.mongodb.net/MovieMania?retryWrites=true&w=majority'
# Change this to a random secure key in production
app.config['JWT_SECRET_KEY'] = 'neeraj'
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb+srv://bishtnrj1418:neeraj@cluster0.ofkqsxc.mongodb.net/MovieMania?retryWrites=true&w=majority'
}
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


# User login endpoint

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


# ================================================================

# movies only get request is importants


# Endpoint to add a new movie
# @app.route('/movies', methods=['POST'])
# def add_movie():
    data = request.json
    movie = Movie(
        Title=data['Title'],
        imdbID=data['imdbID'],
        Year=data['Year'],
        Poster=data['Poster'],
        Type=data['Type']
    )
    movie.save()

    movie_data = {
        'id': str(movie._id),
        'Title': movie.Title,
        "imdbID": movie.imdbId,
        'Year': movie.Year,
        'Poster': movie.Poster,
        "Type": movie.Type
    }

    return jsonify(movie_data), 201

# Endpoint to get all movies


@app.route('/movies', methods=['GET'])
def get_movies():
    movies = Movie.objects.all()

    movie_list = []
    for movie in movies:
        movie_data = {
            'id': str(movie._id),
            'Title': movie.Title,
            "imdbID": movie.imdbID,
            'Year': movie.Year,
            'Poster': movie.Poster,
            "Type": movie.Type
        }
        movie_list.append(movie_data)

    return jsonify(movie_list), 200


# @app.route('/movies/<string:imdbID>', methods=['PUT'])
# def update_movie(imdbID):
#     data = request.json
#     movie = Movie.objects(imdbID=imdbID).first()
#     if not movie:
#         return jsonify({'message': 'Movie not found'}), 404

#     movie.title = data.get('title', movie.title)
#     movie.year = data.get('year', movie.year)
#     movie.type = data.get('type', movie.type)
#     movie.poster = data.get('poster', movie.poster)
#     movie.save()
#     return jsonify(ma.dump(movie))


# @app.route('/movies/<imdbID>', methods=['DELETE'])
# def delete_movie(imdbID):
#     movie = Movie.objects(imdbID=imdbID).first()
#     if not movie:
#         return jsonify({'message': 'Movie not found'}), 404

#     movie.delete()
#     return jsonify({'message': 'Movie deleted successfully'})


# ============================================================
if __name__ == '__main__':
    app.run(debug=True)