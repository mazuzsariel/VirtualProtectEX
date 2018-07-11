import socket
import time


def recvmsg():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
    client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    client.bind(("", 35557))
    while True:
        data, addr = client.recvfrom(1024)
        print("received message: %s"%data)

def sendmsg():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    server.settimeout(0.2)
    message = b"your very important message"
    while True:
        server.sendto(message, ('<broadcast>', 35557))
        print("message sent!")
        time.sleep(1)

    
