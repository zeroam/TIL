import subprocess

proc = subprocess.Popen(
    ['echo', 'Hello World'], stdout=subprocess.PIPE)

out, err = proc.communicate()
print(out.decode('utf8'))