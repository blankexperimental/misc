# -*- encoding: utf-8 -*-

import echo_service_pb2
import tt_channel
import t_controller
import asyncore
import time

# 要返回response的话，需要增加context_map，在response返回时能够找到callback
# 如果出错，直接调用callback

def Callback(response = None):
  print response
  return

if __name__ == "__main__":
  rpc_channel = tt_channel.TestRpcChannel()
  print 'wait...'
  asyncore.loop()
