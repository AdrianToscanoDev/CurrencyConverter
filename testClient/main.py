import zmq
import json

# Get socket to talk to server
context = zmq.Context()
print("Connecting to CurrencyConverter server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

# create a list that holds the data that will be sent
sample_data = ["convert_to_USD", ("currency", "EUR"), ("amount", 100)]

# convert the list to a json string
json_data = json.dumps(sample_data)

# byte encode the data, so it can be sent via socket.send()
byte_data = json_data.encode('utf-8')

# prints to terminal
print("Connected...")
print(f"Sending request: {sample_data} ")

# Sends the request to the microservice
socket.send(byte_data)

# Get the reply.
# NOTE - if converted comes back as "-0.0" - this means the currency conversion does not support the
# original currency. (EUR in this case)
converted = socket.recv()

print(f"Received reply... ")
print(f"This is the converted value :  {converted} ")
