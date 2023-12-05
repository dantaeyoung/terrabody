this assumes [pi-heart](https://github.com/dantaeyoung/pi-heart/) and an rpi5.


## Whisper.cpp

Install whisper.cpp
(More instructions via https://github.com/ggerganov/whisper.cpp/discussions/166)
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

pip install whispercpp


## Piper


Via (https://github.com/rhasspy/piper/tree/master)

1. Download to `piper/piper`
* [amd64](https://github.com/rhasspy/piper/releases/download/v1.2.0/piper_amd64.tar.gz) (64-bit desktop Linux)
* [arm64](https://github.com/rhasspy/piper/releases/download/v1.2.0/piper_arm64.tar.gz) (64-bit Raspberry Pi 4)

2. [Download a voice]([#voices](https://huggingface.co/rhasspy/piper-voices/tree/v1.0.0)) and extract the `.onnx` and `.onnx.json` files
3. Test with `test_piper.py`
   
  
### Install python libraries



 - `sudo apt install python3-pyaudio`??
 - install portaudio (need to build from scratch)
 - `pip install pyaudio`
 - `pip install sounddevice`

## SETUP

gpio_zmq_server.sh and main_switchboard.py communicate to each other via zmq.

 - Run `gpio_zmq_server.sh` as a process via pm2.
 - Run `main_switchboard.py` as a process via pm2.

