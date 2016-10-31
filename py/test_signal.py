# -*- encoding: utf-8 -*-

import signal
import os
# Define signal handler function
def myHandler(signum, frame):
    print("Now, it's the time")
    exit()

# register signal.SIGALRM's handler
signal.signal(signal.SIGINT, myHandler)
while True:
    print('not yet')
