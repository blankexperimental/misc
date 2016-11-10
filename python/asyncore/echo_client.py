# -*- encoding: utf-8 -*-

import asyncore
import socket

class EchoClient(asyncore.dispatcher):
  def __init__(self, host, port, message):
    asyncore.dispatcher.__init__(self)
    self.create_socket(socket.AF_INET, socket.SOCK_STREAM)

    self.message = message
    self.to_send = message
    self.recv_data_list = []

    self.connect((host, port))
    return

  def handle_connect(self):
    print '[client][handle_connect]'
    return

  def handle_close(self):
    print '[client][handle_close]'
    self.close()
    received_message = ''.join(self.recv_data_list)
    print '[client][handle_close]', received_message
    return

  def writable(self):
    print '[client][writable]'
    return bool(self.to_send)

  def readable(self):
    print '[client][readable]'
    return True

  def handle_read(self):
    print '[client][handle_read]'
    data = self.recv(128)
    self.recv_data_list.append(data)
    return

  def handle_write(self):
    print '[client][handle_write]'
    sendn = self.send(self.to_send[:128])
    print '[client][handle_write]sendn:', sendn
    self.to_send = self.to_send[sendn:]
    return

if __name__ == '__main__':
  host = '127.0.0.1'
  port = 36000

  message = open('data.txt', 'r').read()
  print '===send:', len(message)
  c = EchoClient(host, port, message)

  asyncore.loop()
