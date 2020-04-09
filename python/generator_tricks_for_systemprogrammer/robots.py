# robots.py
#
# Find out who has been hitting robots.txt

import socket
from linesdir import lines_from_dir
from apachelog import apache_log

lines = lines_from_dir("access-log*", "www")
log = apache_log(lines)

addrs = {r["host"] for r in log if "robots.txt" in r["request"]}

for addr in addrs:
    try:
        print(socket.gethostbyaddr(addr)[0])
    except socket.herror:
        print(addr)
