from gpiozero import Button, LED
from time import sleep
from signal import pause
import subprocess
import signal
import os


# Function to run a script as a different user
def run_script_as_user(script, username, argument):
    cmd = f'sudo -u {username} python {script} {argument}'
    process = subprocess.Popen(cmd, shell=True, preexec_fn=os.setsid)
    return process

# Function to send SIGINT to a process
def send_sigint(process):
    os.killpg(os.getpgid(process.pid), signal.SIGINT)



# Replace with your script's path and the username
script_path = './recorder_sigterm.py'
argument = 'summon.wav'
username = 'nabu'

# Run the script as a different user
process = run_script_as_user(script_path, username, argument)

# Wait for a while or replace with your logic
sleep(5)  # Replace with desired duration

# Send SIGINT to the script
send_sigint(process)



red = LED(17)
green  = LED(27)

Button.was_held = False

def held(btn):
    btn.was_held = True
    red.on()
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

def just_pressed():
    print("button was pressed not held")

def pressed():
    green.on()

btn = Button(2)

btn.when_held = held
btn.when_released = released
btn.when_pressed = pressed

pause()
