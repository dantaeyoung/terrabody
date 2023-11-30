import zmq
from recorder import Recorder, AudioFile

rec = Recorder(channels=1)

context = zmq.Context()
subsocket = context.socket(zmq.SUB)
subsocket.connect("tcp://localhost:5560")
subsocket.setsockopt_string(zmq.SUBSCRIBE, "")  # Subscribe to all messages
pubsocket = context.socket(zmq.PUB)
pubsocket.connect("tcp://localhost:5559")



while True:
    message = subsocket.recv_string()
    print(message)
    
    if message == "button1_held":
        recfile2 = rec.open("output.wav", 'wb')
        print("STARTING RECORDING")
        recfile2.start_recording()

    if message == "button1_released":
        recfile2.stop_recording() 
        recfile2.close()
        print("STOPPED RECORDING")
        pubsocket.send_string("mouth:saysomething")
        a = AudioFile("output.wav")
        a.play()
        a.close()


