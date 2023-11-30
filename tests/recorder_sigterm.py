import argparse
from recorder import Recorder
import signal
import time
import sys

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Record audio.')
parser.add_argument('rec_filename', help='Output filename for the recording')
args = parser.parse_args()

rec = Recorder(channels=1)


recfile = rec.open(args.rec_filename, 'wb')

def signal_term_handler(signal, frame):
    print('SIGINT!')
    print('Saving the recording to ', args.rec_filename)
    recfile.stop_recording() 
    sys.exit(0)

signal.signal(signal.SIGTERM, signal_term_handler)

try:
    recfile.start_recording()
    time.sleep(600.0)
    recfile.stop_recording() 
    print('Ran up to time limit. Saving the recording to ', args.rec_filename)
except KeyboardInterrupt:
    pass


signal_term_handler(None, None)

signal.pause()

