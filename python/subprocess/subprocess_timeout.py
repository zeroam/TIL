import subprocess


def run_sleep(period):
    proc = subprocess.Popen(['sleep', str(period)])
    return proc

proc = run_sleep(10)
try:
    proc.communicate(timeout=0.1)
except subprocess.TimeoutExpired:
    proc.terminate()
    proc.wait()

print('Exit Status', proc.poll())