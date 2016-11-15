# -*- encoding: utf-8 -*-

import lookup3
import platform

print platform.system()

for i in range(3):
  print lookup3.hash32('a')
  print lookup3.hash32('b')
  print lookup3.hash64('a')
  print lookup3.hash64('b')


