# -*- encoding: utf-8 -*-

import asyncore
import t_parser
import t_setting
import t_controller

class TSession(asyncore.dispatcher):
  def __init__(self, rpc_service, sock, address, acceptor):
    asyncore.dispatcher.__init__(self, sock)
    self.address = address
    self.rpc_service = rpc_service
    self.send_msg_list = []
    self.recv_msg_list = []
    self.rpc_controller = t_controller.TRpcController()
    self.acceptor = acceptor

  def SendData(self, data):
    self.send_buffer_list.append(data)
    return

  def writable(self):
    return len(self.send_msg_list)

  def handle_write(self):
    for msg in self.send_msg_list:
      self.send(msg)
    return

  def readable(self):
    return True

  def Callback(self, call_guid, response):
    response_msg = t_parser.PackResponse(call_guid, response.SerializeToString())
    self.SendData(response_msg)
    return

  # TODO: 目前支持的是单service，需要增加register机制增加多service
  # TODO: 目前消息解析使用最简单的方式，需要细化
  # TODO: 需要增加异常处理
  # TODO: 用method_idx没有method_name做cmd_key兼容性好, method_idx->method_key
  def handle_read(self):
    msg = self.recv(t_setting.BUFF_SIZE)
    print '[session][handle_read]', msg
    call_guid, method_idx, data = t_parser.UnpackRequest(msg)
    method_descriptor = self.rpc_service.GetDescriptor().methods[method_idx]
    request_class = self.rpc_service.GetRequestClass(method_descriptor)
    request = request_class()
    request.ParseFromString(data)
    self.rpc_service.CallMethod(method_descriptor, self.rpc_controller, request,
                                lambda response: self.Callback(call_guid, response))
    return

  def handle_close(self):
    print 'handle_close'
    self.Stop()

  def handle_error(self):
    print 'handle_error'

  def Stop(self):
    print "[session_dict]", self.acceptor.session_dict
    address_key = t_parser.Address2Key(self.address)
    if address_key not in self.acceptor.session_dict:
      print address_key, "not in session_dict"
    else:
      print address_key, "in session_dict"
      self.acceptor.session_dict.pop(address_key)
    self.close()