#/usr/bin/python
#coding:utf-8

'''
__Author__ = 'eyu Fanne'
__Date__ = '2016/9/3'

import os
import re

rootDir = u'F:\慕课大巴2'
rmfile =[u'慕课大巴 - IT学习资源分享社区.url',u'教程目录及说明.txt']

##遍历打印目录下的文件
##匹配到rmfile后删除文件

def Test1(rootDir):
    for root,dirs,files in os.walk(rootDir):
        # print files
        for filespath in files:
            # print filespath  ##打印出所有文件
            if filespath in rmfile or re.findall(r'url$',filespath):
                guanggao_file = os.path.join(root,filespath)
                print guanggao_file
                os.remove(guanggao_file)



if __name__ == '__main__':
    Test1(rootDir)

'''