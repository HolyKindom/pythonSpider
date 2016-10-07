#/usr/bin/python
#coding:utf-8

__Author__ = 'eyu Fanne'
__Date__ = '2016/9/3'

##批量冲命名文件

import os

# 执行重命名功能
path = u'F:\慕课大巴2\徐老师大数据\资料与书籍\Public_PDF\Hadoop'
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path, file)) == True:
        newname = file.replace(u"[IT十八掌www.it18zhang.com]", "")
        os.rename(os.path.join(path, file), os.path.join(path, newname))
        # newname2 = file.replace(u'[mukedaba.com]徐老师大数据－',"")
        # os.rename(os.path.join(path,file),os.path.join(path,newname2))

'[mukedaba.com]徐老师大数据－'