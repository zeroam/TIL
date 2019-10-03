import random, time
from threading import Event, Thread

event = Event()


def waiter(event, nloops):
    for i in range(nloops):
        print('%s. Waiting for the flag to be set.' % (i + 1))
        event.wait()    # Blocks until the flag become true
        print('Wait complete at:', time.ctime())
        event.clear()
        print()

    
def setter(event, nloops):
    for i in range(nloops):
        time.sleep(random.randrange(2, 5))  # Sleeps for some time
        event.set()


threads = []
nloops = random.randrange(3, 6)

threads.append(Thread(target=waiter, args=(event, nloops)))
threads[-1].start()
threads.append(Thread(target=setter, args=(event, nloops)))
threads[-1].start()

for thread in threads:
    thread.join()

print('Add done.')