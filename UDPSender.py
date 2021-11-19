from socket import *


class UDPSender:

    def __init__(self):
        self.ip: str = "127.0.0.1"
        self.port: int = 9999
        self.socket: socket = None

    def connect(self, ip: str, port: int):
        if self.socket is not None:
            self.disconnect()

        self.ip = ip
        self.port = port
        self.socket = socket(AF_INET, SOCK_DGRAM)

    def disconnect(self):
        self.socket.close()

    def send(self, value: str):
        self.socket.sendto(value.encode("utf-8"), (self.ip, self.port))


if __name__ == '__main__':
    sender = UDPSender()
    sender.connect("127.0.0.1", 9999)
    sender.send("abc_5_30")
