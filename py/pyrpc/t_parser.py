# -*- encoding: utf-8 -*-

import struct

def PackRequest(call_guid, method_idx, data):
  msg = ''.join([struct.pack('<I', call_guid),
                 struct.pack('<H', method_idx),
                 data])
  return msg

def UnpackRequest(msg):
  call_guid = int(msg[0:4])
  method_idx = int(msg[4:6])
  data = msg[6:]
  return [call_guid, method_idx, msg]


def PackResponse(call_guid, data):
  msg = ''.join([struct.pack('<I', call_guid),
                 data])
  return msg

def UnpackResponse(msg):
  call_guid = int(msg[0:4])
  data = msg[4:]
  return [call_guid, msg]


Ip2Int = lambda x:sum([256**j*int(i) for j,i in enumerate(x.split('.')[::-1])])

def Address2Key(address):
  ip = address[0]
  port = address[1]
  ip_int = Ip2Int(ip)
  key_str = '%s%s' % (ip_int, port)
  return int(key_str)