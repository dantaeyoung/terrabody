from gpiozero import Button, LED
from time import sleep
from signal import pause
import subprocess
import signal
import os
import zmq


print(">>> STARTING GPIO ZMQ SERVER")

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
    print("[sending] button1_held")

def released(btn):
    if not btn.was_held:
        just_pressed()
    else:
        print("[sending] button1_released")
        socket.send_string("button1_released")
    btn.was_held = False
    red.off()
    green.off()

def just_pressed():
    print("[sending] button1_justpressed")
    socket.send_string("button1_justpressed")

def pressed():
    green.on()

btn = Button(2)

btn.hold_time = 0.2 

btn.when_held = held
btn.when_released = released
btn.when_pressed = pressed

pause()
