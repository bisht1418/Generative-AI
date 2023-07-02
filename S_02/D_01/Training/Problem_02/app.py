from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.debug = True

my_dict = {}


@app.route('/')
def index():
    try:
        # Your code here
        return "Success"
    except Exception as e:
        return f"An error occurred: {str(e)}"


@app.route("/abc")
def home():
    return render_template("index.html", my_dict=my_dict)


@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


@app.route('/create', methods=['GET'])
def create_form():
    return render_template('create.html')


@app.route('/create', methods=['POST'])
def create_entry():
    key = request.form.get('key')
    value = request.form.get('value')
    my_dict[key] = value
    return f'Entry created successfully! ==>{my_dict}'


@app.route('/read')
def read_dictionary():
    return render_template('read.html', my_dict=my_dict)


@app.route('/update', methods=['GET'])
def update_form():
    return render_template('update.html')

# Route to handle form submission and update the dictionary


@app.route('/update', methods=['POST'])
def update_entry():
    # Get the data from the form
    key = request.form.get('key')
    value = request.form.get('value')

    # Check if the key exists in the dictionary
    if key in my_dict:
        # Update the value for the existing key
        my_dict[key] = value
        return 'Entry updated successfully!'
    else:
        return 'Key does not exist in the dictionary!'


@app.route('/delete', methods=['GET'])
def delete_form():
    return render_template('delete.html')

# Route to handle form submission and delete the entry from the dictionary


@app.route('/delete', methods=['POST'])
def delete_entry():
    # Get the data from the form
    key = request.form.get('key')

    # Check if the key exists in the dictionary
    if key in my_dict:
        # Delete the entry for the existing key
        del my_dict[key]
        return 'Entry deleted successfully!'
    else:
        return 'Key does not exist in the dictionary!'


if __name__ == "__main__":
    app.run(use_reloader=True)
