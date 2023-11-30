import zmq

def main():
    context = None
    frontend = None
    backend = None

    try:
        context = zmq.Context()
        # Socket facing clients
        frontend = context.socket(zmq.SUB)
        frontend.bind("tcp://*:5559")
        frontend.setsockopt_string(zmq.SUBSCRIBE, "")

        # Socket facing services
        backend = context.socket(zmq.PUB)
        backend.bind("tcp://*:5560")

        print("STARTING ZMQ SWITCHBOARD")
        zmq.device(zmq.FORWARDER, frontend, backend)
    except Exception as e:
        print(e)
        print("Bringing down zmq device")
    finally:
        if frontend:
            frontend.close()
        if backend:
            backend.close()
        if context:
            context.term()

if __name__ == "__main__":
    main()

