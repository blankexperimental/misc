# -*- encoding: utf-8 -*-

# http://everet.org/python-byte-code.html

import dis

def sayhello():
  print 1
  print 'hello'
  return

dis.dis(sayhello)