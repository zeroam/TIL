# shutdownevt.py
#
# Example of a generator that uses an event to shut down
import os
import time
import threading


def follow(thefile, shutdown=None):
    thefile.seek(0, os.SEEK_END)
    while True:
        if shutdown and shutdown.is_set():
            break
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line


def run(shutdown_event=None):
    lines = follow(open("run/foo/access-log"), shutdown_event)
    for line in lines:
        print(line)

    print("Done")


if __name__ == "__main__":
    shutdown_event = threading.Event()

    # Run the above in a separate thread
    t = threading.Thread(target=run, args=(shutdown_event,))
    t.start()

    # Wait a while then shut down
    time.sleep(60)
    print("Sutting down")

    shutdown_event.set()
