import subprocess
import zmq


context = zmq.Context()
subsocket = context.socket(zmq.SUB)
subsocket.connect("tcp://localhost:5560")
subsocket.setsockopt_string(zmq.SUBSCRIBE, "")  # Subscribe to all messages

command = [
    "echo", "Hello! How are you?",
    "|", "~/heart/github/terrasummon/mouth/piper/piper", "--model", "/heart/github/terrasummon/mouth/piper/voices/en_GB-alan-medium.onnx", "--output-raw",
    "|", "aplay", "-r", "22050", "-f", "S16_LE", "-t", "raw", "-"
]

# Use subprocess to run the command
try:
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode == 0:
        print("Command executed successfully.")
    else:
        print("Error executing the command.")
        print("STDOUT:")
        print(stdout.decode("utf-8"))
        print("STDERR:")
        print(stderr.decode("utf-8"))
except Exception as e:
    print(f"An error occurred: {str(e)}")

while True:
    message = subsocket.recv_string()
    print(message)

    if(message == "mouth:saysomething"):
        print("saysomething")

 
#echo 'Hello! How are you?' | ./piper --model voices/en_GB-alan-medium.onnx --output-raw | aplay -r 22050 -f S16_LE -t raw -
