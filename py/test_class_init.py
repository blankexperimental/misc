# -*- encoding: utf-8 -*-

import sys

class MyTest(object):
  def __init__(self):
    super(MyTest, self).__init__()
    print sys._getframe().f_code.co_name
    self.a = 1

  def __new__(cls, *args, **kwargs):
    print sys._getframe().f_code.co_name
    return super(MyTest, cls).__new__(cls, *args, **kwargs)

  def Dump(self):
    print sys._getframe().f_code.co_name
    print type(sys._getframe())
    print dir(sys._getframe())
    print sys._getframe()
    print sys._getframe(0)
    print sys._getframe(1)
    print sys._current_frames()



t1 = MyTest()
print t1
t1.Dump()
