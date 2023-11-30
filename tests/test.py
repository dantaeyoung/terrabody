from gpiozero import Button, LED
from time import sleep
from signal import pause

red = LED(17)
green  = LED(27)

Button.was_held = False

def held(btn):
    btn.was_held = True
    red.on()
    print("button was held not just pressed")

def released(btn):
    if not btn.was_held:
        just_pressed()
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
