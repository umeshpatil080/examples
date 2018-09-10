import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind('tcp://*:5555')
while 1:
    # Get request
    request = socket.recv()
    # Reply with response
    socket.send('this is anwer to ' + request)