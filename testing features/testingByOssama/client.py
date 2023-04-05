import socket

HOST = input("host address")
PORT= int(input("port number"))#9090
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((HOST,PORT))
msg=input("enter a msg")
client.send(msg.encode("utf-8"))
while msg!="end":
    print(client.recv(1024))
    client.send(msg.encode("utf-8"))
    msg=input("enter a msg")

client.send(msg.encode("utf-8"))
print("client ended")

