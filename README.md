
# (terrasummon)

part of the terra system.

this assumes [pi-heart](https://github.com/dantaeyoung/pi-heart/).











## Whisper.cpp

### Install whisper.cpp
More instructions via https://github.com/ggerganov/whisper.cpp/discussions/166
 - `sudo apt install libsdl2-dev`
In a directory:
  ```
git clone https://github.com/ggerganov/whisper.cpp
cd whisper.cpp
make -j stream
make
make server
./models/download-ggml-model.sh tiny.en
./models/download-ggml-model.sh base.en
```
Daemonize with pm2
- pm2 start ./server --name whisper-server


  
### Install python libraries



 - `sudo apt install python3-pyaudio`??
 - install portaudio (need to build from scratch)
 - `pip install pyaudio`
 - `pip install sounddevice`

## SETUP

gpio_zmq_server.sh and main_switchboard.py communicate to each other via zmq.

 - Run `gpio_zmq_server.sh` as a process via pm2.
 - Run `main_switchboard.py` as a process via pm2.

