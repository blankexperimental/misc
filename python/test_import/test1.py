# -*- encoding: utf-8 -*-

from test import my_test
print my_test.CONST_TEST
my_test.CONST_TEST = 'const test 2'
print my_test.CONST_TEST
print my_test.Klass.a
my_test.Klass.a = 'a2'
print my_test.Klass.a

from test.my_test import Klass
from test.my_test import CONST_TEST
print Klass.a
print CONST_TEST

print '----------------'
# 路径不一样，import的module不一样，import时全局初始化内容会是两份
import sys
sys.path.append('./test')
import my_test
print my_test.CONST_TEST
print my_test.Klass.a


