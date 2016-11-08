# -*- encoding: utf-8 -*-

import echo_service_pb2
import t_server

class MyEchoService(echo_service_pb2.EchoService):

  def __init__(self):
    super(MyEchoService, self).__init__()
    self.service_stub = None

  def Echo(self, rpc_controller, request, callback):
    response = echo_service_pb2.EchoResponse
    response.pong = request.ping
    callback(response)


if __name__ == "__main__":
  pass
