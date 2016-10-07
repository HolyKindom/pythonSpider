#/usr/bin/python
#coding:utf-8

__Author__ = 'eyu Fanne'
__Date__ = '2016/9/3'
##拷贝公众号到各个子目录中

import os
import shutil
import random
import string
##打印出各个子目录，拷贝公众号图片到各个子目录


gongzhonghao = u'D:\\360Tongbu\微信公众号\GirlsOps公众号\girlsops.jpg'
rootDir = u'E:\各大网站视频教程\麦子学院二期'


for root,dirs,files in os.walk(rootDir):
    for name in dirs:
        print(os.path.join(root, name))
        dstdir = os.path.join(root, name)
        shutil.copyfile('%s' %gongzhonghao,'%s\GirlsOps.jpg' %dstdir)


