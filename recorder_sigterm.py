from recorder import Recorder
import signal
import time
import sys

rec = Recorder(channels=1)

recfile = rec.open("output.wav", 'wb')

def signal_term_handler(signal, frame):
    print('SIGINT!')
    print('Saving the recording...')
    recfile.stop_recording() 
    sys.exit(0)

signal.signal(signal.SIGTERM, signal_term_handler)

recfile.start_recording()
time.sleep(500.0)
recfile.stop_recording() 

signal_term_handler(None, None)

signal.pause()

