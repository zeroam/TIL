# query404.py
#
# Find the set of all documents that 404 in a log file

from follow import follow
from linesdir import lines_from_dir
from apachelog import apache_log


def gengrom_queue(thequeue):
    while True:
        item = thequeue.get()
        if item is StopIteration:
            break
        yield item


def sendto_queue(items, thequeue):
    for item in items:
        thequeue.put(item)
    thequeue.put(StopIteration)


def print_r404(log_q):
    log = gengrom_queue(log_q)
    r404 = (r for r in log if r["status"] == 404)
    for r in r404:
        print(r["host"], r["datetime"], r["request"])


if __name__ == "__main__":
    import threading, queue

    log_q = queue.Queue()
    r404_thr = threading.Thread(target=print_r404, args=(log_q,))

    r404_thr.start()

    # finite data
    lines = lines_from_dir("access-log*", "www")

    log = apache_log(lines)
    sendto_queue(log, log_q)
