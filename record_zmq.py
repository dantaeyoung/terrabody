import zmq
from common.recorder import Recorder, AudioFile
from common.pubsub import Pubsub

rec = Recorder(channels=1)

ps = Pubsub(name="record")


while True:
    message = ps.recv_string()
    print(message)
   
    if "gpio--to" in message:

        if "button1_held" in message:
            recfile2 = rec.open("output.wav", 'wb')
            print("STARTING RECORDING")
            recfile2.start_recording()

        if "button1_released" in message:
            recfile2.stop_recording() 
            recfile2.close()
            print("STOPPED RECORDING")
            ps.send_string("record--to--*::recorded")
            #a = AudioFile("output.wav")
            #a.play()
            #a.close()


