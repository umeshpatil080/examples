import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect('tcp://localhost:5555')
socket.send('Hello')
message = socket.recv()
print 'Received reply: %s' % message