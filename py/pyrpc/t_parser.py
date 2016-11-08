# -*- encoding: utf-8 -*-

import struct

def Pack(data):
  data_len = len(data) + 4
  cmd_idx = 0
  send_data = ''.join([struct.pack('<H', data_len),
                       struct.pack('<H', cmd_idx),
                       data])
  return send_data

def Unpack(data):
  cmd_idx = data[:2]
  recv_data = data[2:]
  return [cmd_idx, recv_data]