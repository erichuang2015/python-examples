 #!/usr/bin/env python3
# coding: utf-8

"""查看本机IP."""

import requests
from bs4 import BeautifulSoup


def main():
    url = 'https://www.ipip.net/'
    with requests.Session() as session:
        # 使用socks5代理
        # session.proxies = {
        #     'http': 'socks5://127.0.0.1:1080',
        #     'https': 'socks5://127.0.0.1:1080'
        # }
        r = session.get(url)
        soup = BeautifulSoup(r.text, 'lxml')
        ip = soup.select('div.ip_text')[0].get_text()
        print(ip)


if __name__ == '__main__':
    main()
