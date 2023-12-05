import zmq

class Organmsg():
    def __init__(self, frm ="", to ="", message="", payload={}):
        self.frm = frm
        self.to = to
        self.message = message
        self.payload = payload

    def __contains__(self, m):
        if m in str(s):
            return True
        return False

    def __str__(self):
        return "{}--to--{}::{}:::{}".format(self.frm, self.to, self.message, self.payload)
        #return "{ from:{} to:{}, message:{} payload:{}}".format(self.from, self.to, self.mesage, self.payload



class Pubsub():

    def __init__(self, name=""):
        self.context = zmq.Context()
        self.subsocket = self.context.socket(zmq.SUB)
        self.subsocket.connect("tcp://0.0.0.0:5560")
        self.subsocket.setsockopt_string(zmq.SUBSCRIBE, "")  # Subscribe to all messages
        self.pubsocket = self.context.socket(zmq.PUB)
        self.pubsocket.connect("tcp://0.0.0.0:5559")
        self.name = name

    def recv_string(self):
        obj = self.subsocket.recv_json()
        return obj["messagestring"]

    def receive(self):
        return Organmsg(self.subsocket.recv_json())

    def send_string(self, message):
        obj = { "messagestring": message, "from": self.name }
        return self.pubsocket.send_json(obj)

    def send(self, msg, to=None, payload=None):
        o = Organmsg(frm=self.name, to=to, message=msg, payload=payload)
        return self.pubsocket.send_string(str(o))

    
