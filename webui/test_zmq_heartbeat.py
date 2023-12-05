import zmq
import time

context = zmq.Context()
pubsocket = context.socket(zmq.PUB)
pubsocket.connect("tcp://localhost:5559")

while True:
    print("sending message")
    pubsocket.send_string("heartbeat::test")
    time.sleep(2)
