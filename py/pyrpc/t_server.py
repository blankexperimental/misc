# -*- encoding: utf-8 -*-

import asyncore
import socket
import echo_service_pb2
import t_setting
import t_parser

class TServer(asyncore.dispatcher):
  def __init__(self):
    asyncore.dispatcher.__init__(self)
    self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
    self.set_reuse_addr()
    self.bind((t_setting.HOST, t_setting.PORT))
    self.listen(5)

  def handle_accept(self):
    socket, address = self.accept()
    print '[TServer][handle_accept]', socket, address
    TConnection(socket)

  def handle_close(self):
    print '[server][handle_accept]'
    self.close()
    return

  def handle_error(self):
    return

  def Stop(self):
    self.close()
    return


class TConnection(asyncore.dispatcher):
  def __init__(self, sock):
    asyncore.dispatcher.__init__(self, sock)
    self.send_buffer_list = []
    self.recv_buffer_list = []

  def SendData(self, data):
    self.send_buffer_list.append(data)
    return

  def writable(self):
    return len(self.recv_buffer_list)

  def handle_write(self):
    for data in self.send_buffer_list:
      send_data = t_parser.Pack(data)
      self.send(send_data)
    return

  def readable(self):
    return True

  def handle_read(self):
    data = self.recv(t_setting.BUFF_SIZE)
    data = data[2:]  # 去掉长度
    cmd_idx, recv_data = t_parser.Unpack(data)

  def handle_close(self):
    self.close()

  def handle_error(self):
    self.close()

  def Stop(self):
    self.close()
