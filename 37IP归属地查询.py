#!/usr/bin/env python3
# coding: utf-8

"""IP归属地查询."""

import requests
from lxml import etree


def get_html(ip):
    url = 'http://m.ip138.com/ip.asp'
    kw = {'ip': ip}
    r = requests.get(url, params=kw)
    return r.content


def parse_html(html):
    s = etree.HTML(html)
    addr_info = s.xpath('//p[@class="result"]/text()')
    for n in addr_info:
        print(n)


def main():
    ip = '192.168.1.1'
    html = get_html(ip)
    parse_html(html)


if __name__ == '__main__':
    main()
