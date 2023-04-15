import socket

HOST= "192.168.56.1" #192.168.56.1
PORT= 9090
print(HOST)

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen()

while True:
    comm,addr=server.accept()
    print(f"Connected to {addr}")
    msg=comm.recv(1024).decode("utf-8")
    while msg!="END":
        print(f"Message from client {msg}")
        comm.send("Got your message".encode("utf-8"))
        msg = comm.recv(1024).decode("utf-8")
    comm.close()
    print(f"Connection with {addr} ended")

