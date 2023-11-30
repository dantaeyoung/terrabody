import sounddevice as sd
import numpy as np

# Set the recording duration (in seconds)
duration = 5

print(sd.query_devices())
#sd.default.device = 2
#print(sd.query_devices())
myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
