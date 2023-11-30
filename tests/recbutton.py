from gpiozero import Button, LED
from time import sleep
from signal import pause
from recorder import Recorder


rec = Recorder(channels=1)

red = LED(17)
green  = LED(27)

Button.was_held = False

def held(btn):
    btn.was_held = True
    red.on()
    print("button was held not just pressed")
    recfile = rec.open("output.wav", 'wb')
    recfile.start_recording()
    time.sleep(5.0)
    recfile.stop_recording() 
    print("starting recording")

def released(btn):
    if not btn.was_held:
        just_pressed()
    else:
        print("stopping recording")
    btn.was_held = False
    red.off()
    green.off()

def just_pressed():
    print("button was pressed not held")

def pressed():
    green.on()


btn = Button(2)

btn.when_held = held
btn.when_released = released
btn.when_pressed = pressed

pause()
