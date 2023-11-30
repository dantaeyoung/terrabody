import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555")

while True:
    message = "TriggerFunction1"  # Message to trigger a specific function
    socket.send_string(message)
    time.sleep(1)  # Simulate some work or events

