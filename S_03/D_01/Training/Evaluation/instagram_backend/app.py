from flask import Flask, request

app = Flask(__name__)

posts = [
    {"id": 1, "username": "neeraj", "caption": "neeraj is the best"},
    {"id": 1, "username": "neeraj", "caption": "neeraj is the best"},

]


@app.route("/")
def main():
    return "Welcome to instagram Backend"


@app.route("/lists")
def getPost():
    return posts


@app.route("/lists", methods=["POST"])
def addPost():
    username = request.form["username"]
    caption = request.form["caption"]
    id = request.form["id"]

    post = {"username": username, "caption": caption, "id": id}
    posts.append(post)
    return "Post sucessfully added"


app.run()
