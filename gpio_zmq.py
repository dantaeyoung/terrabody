from gpiozero import Button, LED
from time import sleep
from signal import pause
import subprocess
import signal
import os
import zmq

from pubsub import Pubsub

ps = Pubsub()


red = LED(17)
green  = LED(27)

Button.was_held = False

def held(btn):
    btn.was_held = True
    red.on()
    ps.send_string("button1_held")
    print("[sending] button1_held")

def released(btn):
    if not btn.was_held:
        just_pressed()
    else:
        print("[sending] button1_released")
        ps.send_string("button1_released")
    btn.was_held = False
    red.off()
    green.off()

def just_pressed():
    print("[sending] button1_justpressed")
    #ps.send_string("button1_justpressed")

def pressed():
    green.on()

btn = Button(2)

btn.hold_time = 0.2 

btn.when_held = held
btn.when_released = released
btn.when_pressed = pressed



while True:
    message = ps.recv_string()
    print("received", message)

    if "gpio::led::green::on" in message:
        green.on()

    if "gpio::led::green::off" in message:
        green.off()

