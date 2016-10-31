# -*- code: utf-8 -*-
#from ConstInClass import *
import ConstInClass
#from ConstInFile import *
import ConstInFile
from Utility import *
import time

if __name__ == '__main__':
    class_num = 50  # 对象个数
    const_num = 5   # 每个对象常量个数
    circle_time = 30 # 循环次数
    GenerateInFile(class_num, const_num)
    GenerateInClass(class_num, const_num)

    #print 'const in file:'
    start1 = time.time()
    for x in range(circle_time):
        for i in range(class_num):
            for j in range(const_num):
                const_name = 'ConstInFile.CLASS_' + str(i) + '_CONST_' + str(j)
                #print const_name
                a = eval(const_name)
                #print a
    end1 = time.time()

    #print 'const in class:'
    start2 = time.time()
    for x in range(circle_time):
        for i in range(class_num):
            for j in range(const_num):
                const_name = 'ConstInClass.CLASS_' + str(i) + '.CONST_' + str(j)
                #print const_name
                a = eval(const_name)
                #print a
    end2 = time.time()

    print 'const in file:'
    print end1 - start1
    print 'const in class:'
    print end2 - start2