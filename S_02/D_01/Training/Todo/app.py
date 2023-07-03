from flask import Flask, render_template, request, redirect

app = Flask(__name__)
todos = []


@app.route('/')
def index():
    parameter1 = 'Hello'
    parameter2 = 'World'
    return render_template('index.html', todos=todos)


@app.route('/add', methods=['POST'])
def add():
    todo = request.form.get('todo')
    if todo:
        todos.append(todo)
    return redirect('/')


@app.route('/delete', methods=['POST'])
def delete():
    todo = request.form.get('todo')
    if todo in todos:
        todos.remove(todo)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
