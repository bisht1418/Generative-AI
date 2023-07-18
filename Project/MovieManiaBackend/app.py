from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from pymongo import MongoClient
from bson import ObjectId

# Initialize Flask app and API
app = Flask(__name__)
api = Api(app)

# Set up MongoDB connection
client = MongoClient(
    "mongodb+srv://bishtnrj1418:neeraj@cluster0.ofkqsxc.mongodb.net/?retryWrites=true&w=majority")
# Replace "cine_matrix" with your desired database name
db = client["MovieMania"]
users_collection = db["users"]


def is_email_taken(email):
    return users_collection.find_one({"email": email}) is not None

# Helper function to get user data by username


def get_user_by_email(email):
    return users_collection.find_one({"email": email})

# Resource for user registration


class UserRegistration(Resource):
    def post(self):
        data = request.get_json()

        # Check if the required fields are present in the request
        required_fields = ["username", "password",
                           "gender", "membershipType", "dateOfBirth", "email"]
        for field in required_fields:
            if field not in data:
                return {"message": f"Missing required field: {field}"}, 400

        # Check if the username is already taken
        if is_email_taken(data["email"]):
            return {"message": "Username already taken"}, 400

        # Save the user data to the database
        user_data = {
            "username": data["username"],
            # In a real application, we would hash the password
            "password": data["password"],
            "gender": data["gender"],
            "membershipType": data["membershipType"],
            "dateOfBirth": data["dateOfBirth"],
            "email": data["email"]
        }
        users_collection.insert_one(user_data)

        return {"message": "User registered successfully"}, 201

# Resource for user login


class UserLogin(Resource):
    def post(self):
        data = request.get_json()

        # Check if the required fields are present in the request
        required_fields = ["email", "password"]
        for field in required_fields:
            if field not in data:
                return {"message": f"Missing required field: {field}"}, 400

        # Find the user by email
        user = get_user_by_email(data["email"])

        # Check if the user exists and the password matches (in a real application, we would compare hashed passwords)
        if not user or user["password"] != data["password"]:
            return {"message": "Invalid credentials"}, 401

        # Convert the ObjectId to a string
        user["_id"] = str(user["_id"])

        return {"user": user, "token": "123"}, 200


# Add API resources to routes
api.add_resource(UserRegistration, "/api/register")
api.add_resource(UserLogin, "/api/login")

if __name__ == "__main__":
    app.run(debug=True)
