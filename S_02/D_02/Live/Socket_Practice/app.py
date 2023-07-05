# app.py
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')

# Handler for receiving order status updates


@socketio.on('order_status_update')
def handle_order_status_update(data):
    order_id = data['order_id']
    status = data['status']

    # Broadcast the order status update to all connected clients
    emit('order_status_update', {
         'order_id': order_id, 'status': status}, broadcast=True)


if __name__ == '__main__':
    socketio.run(app)
