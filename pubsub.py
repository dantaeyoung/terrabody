import zmq

class Pubsub():

    def __init__(self):
        self.context = zmq.Context()
        self.subsocket = self.context.socket(zmq.SUB)
        self.subsocket.connect("tcp://localhost:5560")
        self.subsocket.setsockopt_string(zmq.SUBSCRIBE, "")  # Subscribe to all messages
        self.pubsocket = self.context.socket(zmq.PUB)
        self.pubsocket.connect("tcp://localhost:5559")

    def recv_string(self):
        return self.subsocket.recv_string()

    def send_string(self, message):
        return self.pubsocket.send_string(message)
