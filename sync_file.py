# -*- coding: utf-8 -*-

import os
import os.path
import shutil
import json
import time
import re

SRC_ROOT_PATH = r"F:\misc.git\trunk"
DST_ROOT_PATH = r"Z:\github\trunk"

SYNC_FILE_DATA_PATH = './sync_file_data.txt'
ZH_PATTERN = re.compile(u'[\u4e00-\u9fa5]+')

def HasZH(content):
  match = ZH_PATTERN.search(content)
  if match:
    return True
  else:
    return False

def NoNeedProcess(file_name):
  return False

def SaveSyncData(dict_data):
  json_data = json.dumps(dict_data)
  input = open(SYNC_FILE_DATA_PATH, 'w')
  try:
    input.write(json_data)
  finally:
    input.close()
  return

def GetSyncData():
  input = open(SYNC_FILE_DATA_PATH, 'r')
  try:
    json_data = input.read()
  finally:
    input.close()
  if json_data == '':
    return {}
  else:
    dict_data = json.loads(json_data)
    return dict_data

def SyncDir(dir1, dir2):
  print 'process... ', dir1, '>>>' ,dir2
  map_data = GetSyncData()
  print 'map_data len: ', len(map_data)
  # 删除文件
  file_list = map_data.keys()
  for from_file in file_list:
    if not os.path.exists(from_file):
      to_file = from_file.replace(dir1, dir2)
      print "--del--", from_file, to_file
      os.remove(to_file)
      map_data.pop(from_file)

  # 更新文件
  copy_count = 0
  for root, dirs, files in os.walk(dir1):
    for f in files:
      if HasZH(f):
        continue
      else:
        from_file = os.path.join(root, f)
        if NoNeedProcess(from_file):
          continue
        to_file = from_file.replace(dir1, dir2)
        ff_mtime = int(os.stat(from_file).st_mtime)
        old_mtime = map_data.get(from_file, 0)
        # print ff_mtime, old_mtime
        if old_mtime != ff_mtime:
          to_dir = os.path.dirname(to_file)
          if not os.path.exists(to_dir):
            print '---makedir: ', to_dir
            os.makedirs(to_dir)
          print '--sync--', from_file, to_file
          shutil.copy(from_file, to_file)
          copy_count += 1
        map_data[from_file] = ff_mtime
  SaveSyncData(map_data)
  print 'copy_count', copy_count


class TimeIt(object):
  def __init__(self):
    self.last = 0

  def __enter__(self):
    print '---start---'
    self.last = int(time.time()*1000)
    return

  def __exit__(self, exc_type, exc_val, exc_tb):
    now = int(time.time()*1000)
    diff = now - self.last
    print '---end---', diff
    return

def Do():
  with TimeIt() as t:
    dir1 = SRC_ROOT_PATH
    dir2 = DST_ROOT_PATH
    print dir1
    print dir2
    SyncDir(dir1, dir2)

if __name__ == '__main__':
  Do()
