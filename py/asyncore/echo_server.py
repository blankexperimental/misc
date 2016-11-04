# -*- encoding: utf-8 -*-

import asyncore
import socket

class EchoServer(asyncore.dispatcher):
  def __init__(self, host, port):
    asyncore.dispatcher.__init__(self)
    self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
    self.bind((host, port))
    self.listen(5)
    print '[server][init]'
    return

  def handle_accept(self):
    print '[server][handle_accept]'
    # when we get a client connection start a dispatcher for that client
    socket, address = self.accept()
    print '[server][handle_accept]', socket, address
    EchoHandler(socket)
    # self.handle_close()
    return

  def handle_close(self):
    print '[server][handle_accept]'
    self.close()
    return

class EchoHandler(asyncore.dispatcher):
  def __init__(self, sock):
    print '[shandler][handle_accept]'
    asyncore.dispatcher.__init__(self, sock)
    self.data_to_write = []
    return

  def writable(self):
    print '[shandler][writable]'
    response = bool(self.data_to_write)
    return response

  def handle_write(self):
    print '[shandler][handle_write]'
    data = self.data_to_write.pop()
    sendn = self.send(data[:128])
    print '[shandler][handle_write]sendn:', sendn
    if sendn < len(data):
      remaning = data[sendn:]
      # self.data_to_write.insert(0, remaning)
      self.data_to_write.append(remaning)
    if not self.writable():
      self.handle_close()
    return

  def handle_read(self):
    print '[shandler][handle_accept]'
    data = self.recv(128)
    print '[shandler][handle_write]data:', data
    self.data_to_write.insert(0, data)
    return

  def handle_close(self):
    self.close()
    return

if __name__ == '__main__':
  host = '127.0.0.1'
  port = 36000

  s = EchoServer(host, port)
  asyncore.loop()
