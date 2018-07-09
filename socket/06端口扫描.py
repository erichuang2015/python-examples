#!/usr/bin/env python3
# coding: utf-8

import socket


def main():
    activeDegree = dict()
    HOST = socket.gethostbyname(socket.gethostname())
    sk = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
    sk.bind((HOST, 0))
    sk.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    sk.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
    while True:
        c = sk.recvfrom(65535)
        host = c[1][0]
        activeDegree[host] = activeDegree.get(host, 0) + 1
        #if c[1][0] != '169.254.128.193':
        print(c)
    sk.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
    sk.close()


if __name__ == '__main__':
    main()
