from flask import Flask, request
app = Flask(__name__)
app.debug = True  # Enable debug mode


@app.route("/")
def hello():
    return "Hello World! :)"


@app.route('/greet/<username>')
def greet(username):
    return f"Hello, {username}!"

# @app.route('/greet')
# def search():
#     query = request.args.get('q')
#     return f"Hello, {query}!"


@app.route('/farewell/<username>')
def fairwell(username):
    return f"Goodbye, {username}!"


if __name__ == "__main__":
    app.run(use_reloader=True)
