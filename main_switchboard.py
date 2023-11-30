import zmq
from recorder import Recorder, AudioFile

rec = Recorder(channels=1)

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5555")
socket.setsockopt_string(zmq.SUBSCRIBE, "")  # Subscribe to all messages


while True:
    message = socket.recv_string()
    print(message)
    
    if message == "button1_held":
        recfile2 = rec.open("output.wav", 'wb')
        print("STARTING RECORDING")
        recfile2.start_recording()

    if message == "button1_released":
        recfile2.stop_recording() 
        print("STOPPED RECORDING")
        a = AudioFile("output.wav")
        a.play()
        a.close()


