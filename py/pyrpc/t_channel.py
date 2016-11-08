# -*- encoding: utf-8 -*-

import google.protobuf.service
import asyncore
import socket
import t_setting
import t_parser
import t_guid_mgr

class TRpcChannel(asyncore.dispatcher, google.protobuf.service.RpcChannel):
  def __init__(self):
    asyncore.dispatcher.__init__(self)
    google.protobuf.service.RpcChannel.__init__(self)
    self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
    self.is_connected = False
    self.connect((t_setting.HOST, t_setting.PORT))

    self.send_msg_list = []
    self.context_dict = {}

  def handle_connect(self):
    print '[TRpcChannel][handle_connect]'
    self.is_connected = True

  def SendMsg(self, msg):
    print '[TRpcChannel][SendMsg]', msg
    self.send_msg_list.append(msg)
    return

  def CallMethod(self, method_descriptor, rpc_controller,
                 request, response_class, done):
    print '[TRpcChannel][SendMsg]', request, self.is_connected
    if not self.is_connected:
      done(None)
      return

    call_guid = t_guid_mgr.GuidMgr.NewGuid()
    method_idx = method_descriptor.index
    data = request.SerializeToString()
    request_msg = t_parser.PackRequest(call_guid, method_idx, data)
    self.SendMsg(request_msg)
    # TODO: 放到handle_write中
    self.context_dict[call_guid] = [request, response_class, done]
    return

  def handle_close(self):
    self.is_connected = False

  def handle_expt(self):
    self.is_connected = False

  def writable(self):
    print '[TRpcChannel][writable]', len(self.send_msg_list)
    return len(self.send_msg_list)

  def readable(self):
    print '[TRpcChannel][readable]'
    return True

  def handle_read(self):
    msg = self.recv(t_setting.BUFF_SIZE)
    call_guid, method_idx, data = t_parser.UnpackResponse(msg)
    request, response_class, done = self.context_dict.pop(call_guid)
    response = response_class()
    response.ParseFromString(data)
    done(response)
    return

  def handle_write(self):
    for msg in self.send_msg_list:
      self.send(msg)
    self.send_msg_list = []
    return