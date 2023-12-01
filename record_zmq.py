import zmq
from recorder import Recorder, AudioFile
from pubsub import Pubsub

rec = Recorder(channels=1)

ps = Pubsub()


while True:
    message = ps.recv_string()
    print(message)
    
    if message == "button1_held":
        recfile2 = rec.open("output.wav", 'wb')
        print("STARTING RECORDING")
        recfile2.start_recording()

    if message == "button1_released":
        recfile2.stop_recording() 
        recfile2.close()
        print("STOPPED RECORDING")
        ps.send_string("record::recorded")
        #a = AudioFile("output.wav")
        #a.play()
        #a.close()


