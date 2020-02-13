import subprocess

proc = subprocess.Popen(['sleep', '0.3'])
while proc.poll() is None:
    print('Working...')
    # some time-consuming work
    # ...

print('Exit status', proc.poll())
