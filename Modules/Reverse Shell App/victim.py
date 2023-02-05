import socker
import subprocess
host="127.0.0.1"
port=5000
socket=socket.socket()
socket.connect((host, port))
message=socket.recv(1024).decode()
print(message)