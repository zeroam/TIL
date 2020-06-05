# broadcast.py
#
# Broadcast a generator source to a collection of consumers


def broadcast(source, consumers):
    for item in source:
        for c in consumers:
            c.send(item)


class Consumer(object):
    def __init__(self, name):
        self.name = name

    def send(self, item):
        print(self, "got", item)

    def __repr__(self):
        return f"<Counsumer: {self.name}>"


# Example
if __name__ == "__main__":
    c1 = Consumer("c1")
    c2 = Consumer("c2")
    c3 = Consumer("c3")

    from follow import follow

    lines = follow(open("run/foo/access-log"))
    broadcast(lines, [c1, c2, c3])
