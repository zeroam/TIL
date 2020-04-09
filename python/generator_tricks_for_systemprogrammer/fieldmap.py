# retuple.py
#
# Read a sequence of log lines and parse them into a sequence of tuples

import re


def field_map(dictseq, name, func):
    for d in dictseq:
        d[name] = func(d[name])
        yield d


if __name__ == "__main__":
    loglines = open("access-log")

    logpats = r"(\S+) (\S+) (\S+) \[(.*?)\] \"(\S+) (\S+) (\S+)\" (\S+) (\S+)"

    logpat = re.compile(logpats)

    groups = (logpat.match(line) for line in loglines)
    tuples = (g.groups() for g in groups if g)

    colnames = (
        "host",
        "referrer",
        "user",
        "datetime",
        "method",
        "request",
        "proto",
        "status",
        "bytes",
    )

    log = (dict(zip(colnames, t)) for t in tuples)
    log = field_map(log, "status", int)
    log = field_map(log, "bytes", lambda s: int(s) if s != "-" else 0)

    print(next(log))
