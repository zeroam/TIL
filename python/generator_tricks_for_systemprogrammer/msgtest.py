# msgtest.py
#
# A program that sends a message to the sample server in genmessages.py

import socket


def send_msg_udp(msg):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto(msg, ("127.0.0.1", 10000))


def send_msg_tcp(msg):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", 9000))
    s.send(msg)
    s.close()


if __name__ == "__main__":
    # send_msg_udp(b"Hello World")
    send_msg_tcp(b"Hello World")
