 #!/usr/bin/env python3
# coding: utf-8

"""查看本机IP."""

import socks
import socket

import requests
from bs4 import BeautifulSoup


def main():
    # 使用socks5代理, 方法1
    socks.set_default_proxy(socks.SOCKS5, '127.0.0.1', 1080)
    socket.socket = socks.socksocket
    url = 'https://www.ipip.net/'
    with requests.Session() as session:
        # 使用socks5代理, 方法2
        # session.proxies = {
        #     'http': 'socks5://127.0.0.1:1080',
        #     'https': 'socks5://127.0.0.1:1080'
        # }
        r = session.get(url)
        soup = BeautifulSoup(r.text, 'lxml')
        ip = soup.select('div.yourInfo li')[0].get_text()
        print(ip)


if __name__ == '__main__':
    main()
