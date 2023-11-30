

## INSTALL

 - `sudo apt install python3-pyaudio`??
 - install portaudio (need to build from scratch)
 - `pip install pyaudio`
 - `pip install sounddevice`

## SETUP

gpio_zmq_server.sh and main_switchboard.py communicate to each other via zmq.

 - Run `gpio_zmq_server.sh` as a process via pm2.
 - Run `main_switchboard.py` as a process via pm2.

