#coding:utf-8
#极客学院
from bs4 import BeautifulSoup
import requests
import configparser
import time
import json
import re,os,sys
import urllib
import ctypes

plays = ctypes.windll.kernel32

login_session = requests.session()

basedir = u'e:\各大网站视频教程'
CourseFrom = u'极客学院'


headers = {
            "Accept":"application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding":"gzip, deflate",
            "Accept-Language":"zh-CN,zh;q=0.8",
            "Connection":"keep-alive",
            "Content-Length":"109",
            "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
            "Host":"passport.jikexueyuan.com",
            "Origin":"http://passport.jikexueyuan.com",
            "Referer":"http://passport.jikexueyuan.com/sso/login",
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.108 Safari/537.36",
            "X-Requested-With":"XMLHttpRequest"
        }

headers_2 = {
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding":"gzip, deflate, sdch",
            "Accept-Language":"zh-CN,zh;q=0.8",
            "Connection":"keep-alive",
            "Cache-Control":"max-age=0",
            "Host":"www.jikexueyuan.com",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",
            "Upgrade-Insecure-Requests":"1"
        }

class jikeLogin(object):
    def __init__(self,configfile):
        self.loginurl = r'http://passport.jikexueyuan.com/submit/login?is_ajax=1&client=www'

        config = configparser.ConfigParser()
        config.read(configfile)
        configname = 'jikexueyuan'
        self.username = config.get(configname,'uname')
        self.password = config.get(configname,'password')




    def startLogin(self):
        verify_url = r'http://passport.jikexueyuan.com/sso/verify?%s' %int((time.time()))
        verydata = login_session.get(verify_url).content
        file("vcode.gif", 'wb').write(verydata)
        if sys.platform.find('linux') >= 0:
            os.system('xdg-open vcode.gif')
        elif sys.platform.find('darwin') > 0:
            os.startfile('vcode.gif')
        else:
            os.system('call vcode.gif')
        verycode = raw_input('code:')

        login_data = {
            'expire':'7',
            'referer':'http://www.jikexueyuan.com/',
            'uname':self.username,
            'password':self.password,
            'verify':verycode
        }
        s_login = login_session.post(self.loginurl,data=login_data,headers=headers)
        print type(s_login.json())
        for k,v in s_login.json().items():
            print k,v

# 'http://www.jikexueyuan.com/course/391.html',
def getVedio():
    course_dict = {}
    urllist = [
        'http://www.jikexueyuan.com/course/777.html',
        'http://www.jikexueyuan.com/course/821.html',
        'http://www.jikexueyuan.com/course/902.html',
        'http://www.jikexueyuan.com/course/995.html',
        'http://www.jikexueyuan.com/course/1287.html',
        'http://www.jikexueyuan.com/course/1439.html',
        'http://www.jikexueyuan.com/course/1556.html',
        'http://www.jikexueyuan.com/course/1713.html',

    ]

    for class_url in urllist:
        print class_url
        class_text = login_session.get(class_url,headers=headers_2).text
        class_soup = BeautifulSoup(class_text,'lxml')
        class_lists = class_soup.find_all(class_="text-box")  ##获取课程列表

        pro_title = class_soup.find("title").string.split('-')[0].rstrip()  ##获取课程名称
        #pro_title = class_soup.find("title").text.split('-')[0].rstrip()   ##获取课程名称
        print pro_title
        pro_dir = basedir+'\\'+  CourseFrom + '\\' + pro_title ##下载保存的目录
        print pro_dir
        if not os.path.exists(pro_dir):
            os.makedirs(pro_dir)

        num = 1
        for class_i in class_lists:
            class_a = class_i.find_all('a')
            for course in class_a:
                course_url = course.get('href')
                course_title = course.text
                course_text = login_session.get(course_url,headers=headers_2).text
                course_soup = BeautifulSoup(course_text,'lxml')
                course_src = course_soup.find('source')
                downUrl =  course_src.get('src')
                downTitle = pro_dir + '\\' + '%s.%s.mp4' %(num,course_title)
                num += 1
                print downTitle
                print downUrl

                try:
                    pass
                    urllib.urlretrieve(downUrl,downTitle)
                    time.sleep(1)
                except Exception,e:
                    print Exception,":",e
                    print '%s is error url' %downUrl





if __name__=='__main__':
    login = jikeLogin('config.ini')
    login.startLogin()
    getVedio()
    for i in range(5):
        time.sleep(1)
        plays.Beep(500,500)
