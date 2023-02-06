import socket
port_list=[]
banner_list=[]
file=open("ip.txt","r")
ips=file.read()
file.close()
for ip in ips.splitlines():
    print(ip)
    for port in range(1,25):
        try:
            socket=socket.socket()
            socket.connect((str(ip), int(port)))
            banner=socket.recv(1024)
            banner_list.append(str(banner))
            port_list.append(str(port))
            socket.close()
        except:
            pass
print(port_list)
print(banner_list)