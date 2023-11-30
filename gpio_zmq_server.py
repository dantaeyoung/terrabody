from gpiozero import Button, LED
from time import sleep
from signal import pause
import subprocess
import signal
import os
import zmq


context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555")


red = LED(17)
green  = LED(27)

Button.was_held = False

def held(btn):
    btn.was_held = True
    red.on()
    socket.send_string("button1_held")
    print("button was held not just pressed")
    print("starting recording")

def released(btn):
    if not btn.was_held:
        just_pressed()
    else:
        print("stopping recording")
    btn.was_held = False
    red.off()
    green.off()
    socket.send_string("button1_released")

def just_pressed():
    socket.send_string("button1_justpressed")
    print("button was pressed not held")

def pressed():
    green.on()

btn = Button(2)

btn.when_held = held
btn.when_released = released
btn.when_pressed = pressed

pause()
