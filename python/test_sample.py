# -*- encoding: utf-8 -*-

import signal

def SampleHandler(sig_count, current_frame):
  print sig_count, current_frame
  return


signal.signal(signal.SIGVTALRM, SampleHandler)
signal.setitimer(signal.ITIMER_VIRTUAL, 0.01, 0.01)