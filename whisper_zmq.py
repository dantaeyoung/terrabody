import zmq
import os
import requests
from pubsub import Pubsub

ps = Pubsub()

#current_dir = os.path.dirname(os.path.abspath(__file__))

# Define the URL and the file path
url = "http://127.0.0.1:8080/inference"
#relative_file_path = "output.wav"

# Generate the absolute file path
#file_path = os.path.join(current_dir, relative_file_path)

#print(file_path)

# Set the form data payload
payload = {
    "temperature": "0.2",
    "response-format": "json"
}

def transcribe_output():

    files = {'file': ('output.wav', open('output.wav', 'rb'))}

# Make the POST request
    try:
        response = requests.post(url, data=payload, files=files)
        if response.status_code == 200:
            print("Request successful.")
            print(response.json())
            return response.json()
        else:
            print(f"Request failed with status code {response.status_code}.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")




##################


while True:
    message = ps.recv_string()
    print("received", message)
    
    if message == "record::recorded":
        print("yooo")
        ps.send_string("gpio::led::green::on")
        res = transcribe_output()
        ps.send_string("gpio::led::green::off")
        restext = res['text'].strip()

        ps.send_string("transcribed::"+restext)


