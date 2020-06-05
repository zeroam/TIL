# netsend.py
#
# Consume items and send them to a remote machine

import socket, pickle

from broadcast import broadcast
from follow import follow
from apachelog import apache_log


class NetConsumer(object):
    def __init__(self, addr):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect(addr)

    def send(self, item):
        pitem = pickle.dumps(item)
        self.s.sendall(pitem)

    def close(self):
        self.s.close()


# A class that sends 404 requests to another host
class Stat404(NetConsumer):
    def send(self, item):
        if item["status"] == 404:
            super().send(item)


if __name__ == "__main__":
    stat404 = Stat404(("127.0.0.1", 15000))

    lines = follow(open("run/foo/access-log"))
    log = apache_log(lines)
    broadcast(log, [stat404])
