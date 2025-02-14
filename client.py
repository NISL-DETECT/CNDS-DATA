#!/usr/bin/python
#-*- coding:utf-8 -*-
import socket
import sys

def main():
    # You can change the url which you want to test here to detect.
    url = sys.argv[1]
    hostname, sld, tld, port = 'www', 'integralist', 'co.uk', 80
    target = '{}.{}.{}'.format(hostname, sld, tld)

    # create an ipv4 (AF_INET) socket object using the tcp protocol (SOCK_STREAM)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect the client
    # client.connect((target, port))
    client.connect(('202.112.51.36', 9998))

    # send some data (in this case a HTTP GET request)
    #client.send('GET /index.html HTTP/1.1\r\nHost: {}.{}\r\n\r\n'.format(sld, tld))
    #An example of black webpage in Chinese.
    #client.send('http://www.66kj.com'.format(sld,tld))
    #An example of white webpage in Chinese.
    #client.send('http://news.qq.com/world_index.shtml'.format(sld,tld))
    client.send(url.format(sld,tld))

    # receive the response data (4096 is recommended buffer size)
    response = client.recv(4096)

    print(response)

if __name__ == '__main__':
    main()
