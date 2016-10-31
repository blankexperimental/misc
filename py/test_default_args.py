# -*- encoding: utf-8 -*-
"""
NOTE: Python中很奇葩的一个地方是它的函数的默认参数的值，仅仅在def语句执行的时候计算一次
"""

def PackItem(item, pkg = []):
  pkg.append(item)
  return pkg

l = [100, 200]

PackItem(300, l)
print l

pkg = PackItem(1)
print pkg

pkg = PackItem(2)
print pkg

pkg = PackItem(3)
print pkg

