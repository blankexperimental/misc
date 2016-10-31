# -*- encoding: utf-8 -*-

import sys

class Singleton(object):
  def __new__(cls, *args, **kwargs):
    if hasattr(cls, '_instance'):
      return cls._instance
    cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
    return cls._instance

class MyTest(Singleton):
  def __init__(self):
    self.a = 1

  def Dump(self):
    print self.a

t1 = MyTest()
t2 = MyTest()

print id(t1)
print id(t2)

t1.Dump()
t2.Dump()

t1.a = 2

t1.Dump()
t2.Dump()
