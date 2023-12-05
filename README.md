
# (terrasummon)

A Terracomputer is a computer for a wizard. 

Terrabody is made of a Body With Organs. 

An Organ has a particular function. It receives input, chews on it, digests, and then spits it out into an output. 

Each organ listens. 
If it receives a request, it chews and digests, then replies. 
Sometimes, it occasionally announces, like burping into the air. 
Sometimes, it requests something from another organ in order to chew better. 

Organs are pretty independent. Anything about an internal state, it burps. If it wants something specific to happen, it requests. 

In broadcast form: an organ its name + announcement + payload


part of the terra system.

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

  
### Install python libraries



 - `sudo apt install python3-pyaudio`??
 - install portaudio (need to build from scratch)
 - `pip install pyaudio`
 - `pip install sounddevice`

## SETUP

gpio_zmq_server.sh and main_switchboard.py communicate to each other via zmq.

 - Run `gpio_zmq_server.sh` as a process via pm2.
 - Run `main_switchboard.py` as a process via pm2.

