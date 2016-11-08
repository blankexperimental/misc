# -*- encoding: utf-8 -*-

import echo_service_pb2
import t_channel
import t_controller

# 要返回response的话，需要增加context_map，在response返回时能够找到callback
# 如果出错，直接调用callback

def Callback(response = None):
  print response
  return

if __name__ == "__main__":
  rpc_channel = t_channel.TRpcChannel()
  service_stub = echo_service_pb2.ServerService_Stub(rpc_channel)
  request = echo_service_pb2.EchoRequest()
  request.ping = 'test1'

  rpc_controller = t_controller.TRpcController
  callback = Callback
  service_stub.Echo(service_stub, rpc_controller, request, callback)