import subprocess
from time import time


def run_sleep(period):
    proc = subprocess.Popen(['sleep', str(period)])
    return proc

start = time()
proc = run_sleep(10)
proc.wait()
end = time()

print(f'Exit Status {proc.poll()} in {end - start:.3f}s')