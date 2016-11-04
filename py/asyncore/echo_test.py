# -*- encoding: utf-8 -*-

import echo_server
import echo_client
import asyncore
import socket
import time

if __name__ == '__main__':
  host = '127.0.0.1'
  port = 36000

  message = open('data.txt', 'r').read()
  print '-------------------------'
  print message
  print '-------------------------'

  s = echo_server.EchoServer(host, port)
  time.sleep(3)
  c = echo_client.EchoClient(host, port, message)

  asyncore.loop()


