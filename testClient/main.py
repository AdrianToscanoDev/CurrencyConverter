import zmq
import json

# Get socket to talk to server
context = zmq.Context()
print("Connecting to CurrencyConverter server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

# create a list that holds the data that will be sent
data = ["convert_to_USD", ("currency", "asdfk"), ("amount", 100)]
json_data = json.dumps(data)
byte_data = json_data.encode('utf-8')

# Request message
print("Connected...")
print(f"Sending request: {data} ")
socket.send(byte_data)

# Get the reply.
reply = socket.recv()
print(f"Received reply... ")
print(f"This is the converted value :  {reply} ")
