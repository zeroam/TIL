#!/bin/env python
import typing
import requests
import getmac


def mac_info(mac_addr: str) -> typing.Optional[str]:
    url = f"https://api.macvendors.com/{mac_addr}"
    resp = requests.get(url)

    result = None

    if resp.ok:
        result = resp.text
        print(result)
    else:
        print("Not Found")

    return result


if __name__ == "__main__":
    local_mac_addr = getmac.get_mac_address()
    mac_info(local_mac_addr)
