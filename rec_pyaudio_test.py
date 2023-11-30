import pyaudio
import wave

# Set the recording duration (in seconds)
duration = 3

# Set the sample rate and the output filename
sample_rate = 44100  # Standard audio CD quality
output_filename = "recorded_audio.wav"

p = pyaudio.PyAudio()

stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=sample_rate,
                input=True,
                frames_per_buffer=1024)

print("Recording...")

frames = []

for _ in range(0, int(sample_rate / 1024 * duration)):
    data = stream.read(1024)
    frames.append(data)

print("Recording finished.")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(output_filename, 'wb')
wf.setnchannels(1)
wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
wf.setframerate(sample_rate)
wf.writeframes(b''.join(frames))
wf.close()

print("Audio saved to", output_filename)

