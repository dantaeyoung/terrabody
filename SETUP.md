## Hardware:

- Raspberry Pi 5 (ideally 8GB ram)
- USB microphone
- USB speaker
- GPIO inputs (buttons and LEDs)
 - (for detailed info, see `gpio_zmq.py`) 
  

## Pi-heart

Install with [pi-heart](https://github.com/dantaeyoung/pi-heart/)


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

## Pipenv

- `pipenv install`

## SETUP

Use `pm2` to run:

- `pm2 start zmq_switchboard.py`
- `pm2 start gpio.zmq.sh`
- `pm2 start record_zmq.py`
- `pm2 start whisper_zmq.py`
- `cd piper && pm2 start piper_zmq.py`
- ` pm2 start "pipenv run openai_interface.py" --name openai_interface.py`
 
