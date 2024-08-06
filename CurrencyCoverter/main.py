import time
import zmq
import json
from currency_converter import CurrencyConverter

# Get socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

# define conversion function
def convert_data(rcv_data):
    # give the illusion that we are doing something
    time.sleep(3)

    # convert the byte data to a JSON string
    json_data = rcv_data.decode('utf-8')

    # convert the json data to a python object
    data = json.loads(json_data)

    # get the value you want to convert
    convertValue = data[2][1]

    # get the currency type that will be converted
    og_currencyType = data[1][1]

    # get the original currency type (for now, all requests will be converted to USD)
    new_currencyType = "USD"

    # call CurrencyConverter and receive the converted amount (round it)
    converter = CurrencyConverter()

    # catch error if currencyType is invalid (or CurrencyConverter does not support it)
    try:
        convertedAmount = round(converter.convert(convertValue, og_currencyType, new_currencyType), 2)
    except ValueError as e:
        print(f"Error: {e}")
        convertedAmount = -0.0

    return convertedAmount

# print to terminal
print("Waiting for a request... ")

while True:
    #  Wait for next request from client
    byte_data = socket.recv()
    print(f"Data received: {byte_data}")

    # get the final converted value
    convertedValue = convert_data(byte_data)

    # convert the final value back to byte data
    convertedValue_json = json.dumps(convertedValue)
    convertedValue_asByte = convertedValue_json.encode('utf-8')

    #  Send reply back to client
    print(f"Sending back the converted value: { convertedValue_asByte }\n")
    socket.send(convertedValue_asByte)
