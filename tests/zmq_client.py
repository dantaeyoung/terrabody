import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5555")
socket.setsockopt_string(zmq.SUBSCRIBE, "")  # Subscribe to all messages

while True:
    message = socket.recv_string()
    
    # Check if the received message corresponds to the function you want to trigger
    if message == "TriggerFunction1":
        # Call the function you want to trigger
        print("Function 1 triggered.")

    print(message)
    # Add more conditionals for other functions as needed

