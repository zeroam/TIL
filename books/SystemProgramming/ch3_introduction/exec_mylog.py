#!/bin/env python
import os
import mylog

logfile = "/var/log/syslog"
file_length = os.path.getsize(logfile)
# 메시지 로그의 중간부터 추적
mylog.printlog(logfile, "fail", int(file_length / 2), 3, 5)
