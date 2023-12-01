from recorder import Recorder, AudioFile
from pubsub import Pubsub

ps = Pubsub()


while True:
    message = ps.recv_string()
    print(message)
    
    if "(play::repeat)" in message:
        a = AudioFile("output.wav")
        a.play()
        a.close()


