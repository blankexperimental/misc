# -*- encoding: utf-8 -*-

import spooky
import platform

print platform.system()

for i in range(3):
  print spooky.hash32('a')
  print spooky.hash32('b')
  print spooky.hash64('a')
  print spooky.hash64('b')


