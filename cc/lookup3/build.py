# -*- encoding: utf-8 -*-

import os
import os.path
import shutil

print "-------------building-------------"
os.system("python setup.py build")
print "-------------copying-------------"
shutil.copy("./build/lib.win32-2.7/lookup3.pyd", "./lookup3.pyd")
print "-------------test-------------"
os.system("python test.py")
print "-------------finish-------------"