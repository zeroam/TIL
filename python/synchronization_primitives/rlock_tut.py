import threading

num = 0
lock = threading.Lock()

# lock.acquire()
# num += 1
# lock.acquire()
# num += 2
# lock.release()


# With RLock, that problem doesn't happen
lock = threading.RLock()

lock.acquire()
num += 3
lock.acquire()  # This won't block
num += 4
lock.release()
lock.release()  # You need to call release once for each call to acquire

print(num)