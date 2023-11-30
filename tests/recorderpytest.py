from recorder import Recorder
import time

rec = Recorder(channels=1)

recfile2 = rec.open("output.wav", 'wb')
recfile2.start_recording()
time.sleep(5.0)
recfile2.stop_recording() 
