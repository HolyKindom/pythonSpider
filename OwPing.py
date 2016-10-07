# /usr/bin/python
#coding:utf-8

__Date__ = "2016-07-25 13:08"
__Author__ = 'eyu Fanne'

#coding:utf-8
import ctypes
import time
plays = ctypes.windll.kernel32

for i in range(5):
    time.sleep(1)
    plays.Beep(500,5000)