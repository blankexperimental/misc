# -*- encoding: utf-8 -*-

# test python byte code
# ref: http://everet.org/python-byte-code.html

import dis

def sayhello():
  print 1
  print 'hello'
  return

dis.dis(sayhello)