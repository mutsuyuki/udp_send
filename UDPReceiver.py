from socket import *


class UDPReceiver:

    @staticmethod
    def create(port):
        buf_size = 8192
        sock = socket(AF_INET, SOCK_DGRAM)
        sock.bind(("", port))
        while True:
            data, (from_ip, from_port) = sock.recvfrom(buf_size)
            yield data.decode("utf-8")


if __name__ == '__main__':
    receiver = UDPReceiver.create(9999)
    while True:
        received_data = next(receiver)
        print("received ->   " + received_data)
