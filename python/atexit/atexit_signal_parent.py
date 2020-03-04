import os
import signal
import subprocess
import time

proc = subprocess.Popen(['python', './atexit_signal_child.py'])
print('PARENT: Pausing before sending signal...')
time.sleep(1)
print('PARENT: Signaling child')
os.kill(proc.pid, signal.SIGTERM)
