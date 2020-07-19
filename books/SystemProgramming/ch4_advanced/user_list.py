#!/bin/env python
from subprocess import PIPE, Popen


def exec_cmd(cmd: str, encoding="utf-8") -> str:
    p = Popen(cmd, shell=True, stdout=PIPE)
    ret, _ = p.communicate()
    return ret.decode(encoding)


def grep_login_defs(keyword: str) -> str:
    ret = exec_cmd(f"grep '{keyword}' /etc/login.defs")
    return ret.split()[1]


def get_accounts() -> list:
    min_u = grep_login_defs("^UID_MIN")
    max_u = grep_login_defs("^UID_MAX")

    cmd = (
        f"awk -F':' -v 'min={min_u}' -v 'max={max_u}' "
        "'{ if ( $3 >= min && $3 <= max ) print $1 }' /etc/passwd"
    )
    return exec_cmd(cmd).split()


if __name__ == "__main__":
    accounts = get_accounts()
    for account in accounts:
        print(account)
