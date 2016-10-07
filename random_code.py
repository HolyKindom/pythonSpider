#/usr/bin/python
#coding:utf-8

__Author__ = 'eyu Fanne'
__Date__ = '2016/8/29'

'''
简短地生成随机密码，包括大小写字母、数字，可以指定密码长度
'''
#生成随机密码
import random
import string
#python3中为string.ascii_letters,而python2下则可以使用string.letters和string.ascii_letters
def GenPassword(length):
    chars=string.ascii_letters+string.digits
    return ''.join([random.choice(chars) for i in range(length)])#得出的结果中字符会有重复的
    #return ''.join(random.sample(chars, 15))#得出的结果中字符不会有重复的
if __name__=="__main__":
    #生成10个随机密码
    for i in range(30):
        #密码的长度为15
        print GenPassword(6)