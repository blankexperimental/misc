# -*- encoding: utf-8 -*-

import sys
import struct
import binascii

def main(argv):
  data = 'abcd'
  data_len = len(data)
  id1 = 1
  total_len = data_len + 4
  format = '<II%ds' % data_len
  pack_data = struct.pack(format, total_len, id1, data)
  print binascii.hexlify(pack_data)

  unpack_data = struct.unpack(format, pack_data)
  print unpack_data

  size, id = struct.unpack('<II', pack_data[:8])
  print size, id
  data_len = size - 4
  data = struct.unpack('<%ds' % data_len, pack_data[8:])[0]
  print data

if __name__ == '__main__':
  main(sys.argv)