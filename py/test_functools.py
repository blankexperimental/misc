# -*- encoding: utf-8 -*-

import functools
import sys

print '--------------------------'
def dec1(a, b):
  """dec1 docstring"""
  def _dec1(func):
    """_dec1 docstring"""
    def __dec1(*args):
      """__dec1 docstring"""
      print 'start', sys._getframe().f_code.co_name, a, b
      func(*args)
      print 'end', sys._getframe().f_code.co_name
    return __dec1
  return _dec1

@dec1(1, 2)
def func1():
  """func1 docstring"""
  print sys._getframe().f_code.co_name

func1()
print func1.__doc__
print func1.__name__

print '--------------------------'

def dec2(a, b):
  def _dec2(func):
    @functools.wraps(func)
    def __dec2(*args):
      print 'start', sys._getframe().f_code.co_name, a, b
      func(*args)
      print 'end', sys._getframe().f_code.co_name
    return __dec2
  return _dec2

@dec2(1, 2)
def func2():
  """func2 docstring"""
  print sys._getframe().f_code.co_name

func2()
print func2.__doc__
print func2.__name__

print '--------------------------'


def dec3(func):
  @functools.wraps(func)
  def _dec3(*args):
    print 'start', sys._getframe().f_code.co_name
    func(*args)
    print 'end', sys._getframe().f_code.co_name
  return _dec3

@dec3
def func3():
  """func3 docstring"""
  print sys._getframe().f_code.co_name

func3()
print func3.__doc__
print func3.__name__


print '----------------------------'

def my_decorator(func):
  @functools.wraps(func)
  def wrapper(*args, **kwargs):
    print('Calling decorated function...')
    return func(*args, **kwargs)

  return wrapper \

@my_decorator
def example():
  """example docstring"""
  print('Called example function')


print(example.__name__, example.__doc__)