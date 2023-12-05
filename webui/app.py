from flask import Flask, render_template, request
from flask_socketio import SocketIO
import sys
sys.path.append('../')
from common.pubsub import Pubsub

app = Flask(__name__)
socketio = SocketIO(app)

ps = Pubsub()

@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('message_from_client')
def handle_message(message):
    print("received messaage", message)
    # Broadcast the message to all subscribers via ZeroMQ
    ps.send_string(message)

def listen_for_zmq_messages():
    while True:
        zmq_message = ps.recv_string()
        print(f'Message from ZeroMQ: {zmq_message}')
        socketio.emit('message_from_server', zmq_message)

if __name__ == '__main__':
    socketio.start_background_task(listen_for_zmq_messages)
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)


