from subprocess import Popen, PIPE

cmd = "echo hello world"
p = Popen(cmd, shell=True, stdout=PIPE)
ret, err = p.communicate()