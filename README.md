**Communication Contract**

**How to REQUEST data (see testClient main.py file)**: 
1) Setup the socket
 - ![image](https://github.com/user-attachments/assets/476b5195-9a10-4f99-a713-3963ca41ea8b)

2) Convert the request to a JSON string
3) Byte encode the JSON string
4) Send request via : socket.send(byte_encoded_string)
5) example call :
   - ![image](https://github.com/user-attachments/assets/fc927d11-be81-4c9c-a119-46fd3883cf54)


**How to RECEIVE data (see testClient main.py file)**: 
1) data is received via socket.recv()
   - example: converted = socket.recv()
   - This saves the response under the variable "converted"
2) If the response is "-0.0", this means the requested data is either invalid or not supported.

Additional Notes:
- Download CurrencyConverter
- main.py must be running for the request to be received and the response sent. 

UML Diagram: 
![image](https://github.com/user-attachments/assets/45ed819a-1a6a-4107-b80c-8b0ff7a2cef6)
