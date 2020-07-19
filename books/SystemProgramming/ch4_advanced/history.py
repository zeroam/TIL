#!/bin/env python
from argparse import ArgumentParser
from datetime import datetime, timedelta
from collections import Counter

from user_list import exec_cmd, get_accounts


def get_parser() -> ArgumentParser:
    parser = ArgumentParser()

    subparsers = parser.add_subparsers(dest="command", description="history options")

    subparsers.add_parser("all", help="show all history")

    new_parser = subparsers.add_parser("new", help="show new history")
    new_parser.add_argument("num", type=int, nargs="?", default=10, help="number to show")

    frequent_parser = subparsers.add_parser("freq", help="show frequent history")
    frequent_parser.add_argument("count", type=int, nargs="?", default=5, help="number to show")

    date_parser = subparsers.add_parser("date", help="show specific date history before, after one hour")
    date_parser.add_argument("year", type=int, help="year of the history")
    date_parser.add_argument("month", type=int, help="month of the history")
    date_parser.add_argument("day", type=int, help="day of the history")
    date_parser.add_argument("hour", type=int, help="hour of the history")

    return parser


def history(account: str) -> list:
    # env_cmd = "HISTTIMEFORMAT='%F %T '"
    # cmd = f"sudo -u {account} {env_cmd} bash -i -c 'history -r;history'"
    cmd = f"sudo -u {account} zsh -c 'cat ~/.zsh_history'"
    ret = exec_cmd(cmd)
    commands = _preproc_history(ret)

    return list(commands)


def _preproc_history(result: str) -> list:
    splited_command = map(lambda x: _split_history(x), result.split("\n"))
    splited_command = filter(lambda x: x[0] and x[1], splited_command)

    for command in splited_command:
        yield command


def _split_history(string: str) -> (datetime, str):
    tmp = string.strip()

    time_end = tmp.find(":", 1)
    cmd_start = tmp.find(";")
    if time_end == -1:
        return None, None

    time = int(tmp[1:time_end])
    date = datetime.fromtimestamp(time)
    cmd = tmp[cmd_start + 1:]

    return date, cmd


def history_all(accounts: list) -> None:
    for account in accounts:
        print(f"계정: {account}")

        history_list = history(account)
        _print_history(history_list)


def history_new(accounts: list, num: int) -> None:
    for account in accounts:
        print(f"계정: {account}")

        history_list = history(account)

        history_list.sort(key=lambda x: x[0], reverse=True)
        _print_history(history_list[:num])


def history_freq(accounts: list, num: int) -> None:
    for account in accounts:
        print(f"계정: {account}")

        history_list = history(account)

        command_list = []
        for _, command in history_list:
            command_list.append(command)

        counter = Counter(command_list)
        words = ["st", "nd", "rd", "th"]
        for i, (command, freq) in enumerate(counter.most_common(num)):
            if i < 3:
                word = f"{i + 1:3}{words[i]}"
            else:
                word = f"{i + 1:3}{words[3]}"

            print(f"{'':2}{word}: {command} ({freq})")
        print("-" * 70)



def history_date(accounts: list, date: datetime) -> None:
    start_date = date - timedelta(hours=1)
    end_date = date + timedelta(hours=1)

    print(f"{start_date} ~ {end_date} 까지의 히스토리")
    for account in accounts:
        print(f"계정: {account}")

        history_list = history(account)

        results = filter(lambda x: start_date <= x[0] < end_date, history_list)
        _print_history(list(results))


def _print_history(history_list: list) -> None:
    if len(history_list) == 0:
        print("\t기록된 이력없음")
        return

    for time, command in history_list:
        print(f"  {time} {command}")
    print("-" * 70)


if __name__ == "__main__":
    parser = get_parser()
    args = parser.parse_args()

    accounts = get_accounts()
    if args.command == "all":
        history_all(accounts)
    elif args.command == "new":
        history_new(accounts, args.num)
    elif args.command == "freq":
        history_freq(accounts, args.count)
    elif args.command == "date":
        history_date(accounts, datetime(args.year, args.month, args.day, args.hour))
    else:
        parser.error("option not set")
