import sounddevice as sd
import numpy as np

# Set the recording duration (in seconds)
duration = 5

sd.default.device = 2

def audio_callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    if indata.any():
        # Save the audio data to a NumPy array or process it as needed
        audio_data.append(indata.copy())

audio_data = []
with sd.InputStream(callback=audio_callback):
    sd.sleep(int(duration * 1000))

# Convert the recorded audio data to a NumPy array
audio_data = np.concatenate(audio_data, axis=0)

# You can now save or process the recorded audio data as needed
# For example, save it to a WAV file using scipy:
from scipy.io import wavfile

# Specify the output filename
output_filename = "recorded_audio.wav"

# Save the audio data to a WAV file
wavfile.write(output_filename, 44100, audio_data.astype(np.int16))

