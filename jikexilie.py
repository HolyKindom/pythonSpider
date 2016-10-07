##下载即可学院的系列教材

import requests,configparser,os,sys,time,urllib
from bs4 import BeautifulSoup


login_session = requests.session()


xilei_headers={
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding":"gzip, deflate, sdch",
            "Accept-Language":"zh-CN,zh;q=0.8",
            "Connection":"keep-alive",
            "Cache-Control":"max-age=0",
            "Host":"www.jikexueyuan.com",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",
            "Upgrade-Insecure-Requests":"1"
        }

login_headers = {
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

xilei_url = r'http://www.jikexueyuan.com/path/nodejs/?huodong=kuaixun_0328'

basedir = u'D:\各大网站视频教程'
CourseFrom = u'极客学院'


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
        s_login = login_session.post(self.loginurl,data=login_data,headers=login_headers)
        print type(s_login.json())
        for k,v in s_login.json().items():
            print k,v


def getVedio():
    course_dict = {}
    urllist = ['http://www.jikexueyuan.com/course/1374.html',
                'http://www.jikexueyuan.com/course/1410.html',
                'http://www.jikexueyuan.com/course/1520.html',
                'http://www.jikexueyuan.com/course/1638.html',
                'http://www.jikexueyuan.com/course/779.html ',
                'http://www.jikexueyuan.com/course/842.html ',
                'http://www.jikexueyuan.com/course/997.html ',
                'http://www.jikexueyuan.com/course/1919.html',
                'http://www.jikexueyuan.com/course/2301.html',
                'http://www.jikexueyuan.com/course/1976.html',
                'http://www.jikexueyuan.com/course/1905.html',
                'http://www.jikexueyuan.com/course/2440.html',
                'http://www.jikexueyuan.com/course/1722.html',
                'http://www.jikexueyuan.com/course/1518.html',
                'http://www.jikexueyuan.com/course/2052.html',
                'http://www.jikexueyuan.com/course/2373.html',
                'http://www.jikexueyuan.com/course/2352.html',
                'http://www.jikexueyuan.com/course/2561.html',
                'http://www.jikexueyuan.com/course/1663.html',
                'http://www.jikexueyuan.com/course/1631.html',
                'http://www.jikexueyuan.com/course/1726.html',
                'http://www.jikexueyuan.com/course/1884.html',
                'http://www.jikexueyuan.com/course/1972.html',
                'http://www.jikexueyuan.com/course/2044.html',
                'http://www.jikexueyuan.com/course/2065.html',
                'http://www.jikexueyuan.com/course/2072.html',
                'http://www.jikexueyuan.com/course/2155.html',
                'http://www.jikexueyuan.com/course/2228.html',
                'http://www.jikexueyuan.com/course/2281.html',
                'http://www.jikexueyuan.com/course/2386.html',
                'http://www.jikexueyuan.com/course/2424.html',
                'http://www.jikexueyuan.com/course/2457.html',
                'http://www.jikexueyuan.com/course/2276.html',
                'http://www.jikexueyuan.com/course/2252.html',
                'http://www.jikexueyuan.com/course/723.html ',
                'http://www.jikexueyuan.com/course/797.html ',
                'http://www.jikexueyuan.com/course/967.html ',
                'http://www.jikexueyuan.com/course/1332.html',
                'http://www.jikexueyuan.com/course/2288.html',]
    # urllist = [r'http://www.jikexueyuan.com/course/876.html']

    for class_url in urllist:
        #print class_url
        class_text = login_session.get(class_url,headers=login_headers).text
        class_soup = BeautifulSoup(class_text,'lxml')
        class_lists = class_soup.find_all(class_="text-box")  ##获取课程列表
        pro_title = class_soup.find("title").text.split('-')[0]   ##获取课程名称
        pro_dir = basedir+'\\'+  CourseFrom + '\\' + pro_title ##下载保存的目录
        if not os.path.exists(pro_dir):
            os.makedirs(pro_dir)

        num = 1
        for class_i in class_lists:
            class_a = class_i.find_all('a')
            for course in class_a:
                course_url = course.get('href')
                course_title = course.text
                course_text = login_session.get(course_url,headers=login_headers).text
                course_soup = BeautifulSoup(course_text,'lxml')
                course_src = course_soup.find('source')
                downUrl =  course_src.get('src')
                downTitle = pro_dir + '\\' + '%s.%s.mp4' %(num,course_title)
                num += 1
                print downTitle,downUrl

                try:
                    pass
                    urllib.urlretrieve(downUrl,downTitle)
                    time.sleep(1)
                except Exception,e:
                    print Exception,":",e
                    print '%s is error url' %downUrl


def xilieDown(xileiurl):
    xilie_text = requests.get(xileiurl,headers=xilei_headers).text
    xilie_soup = BeautifulSoup(xilie_text,'lxml')
    h2_a = xilie_soup.find_all('h2')

    for i_a in h2_a:
        if i_a.a:
            print i_a.text,i_a.a['href']
        else:
            print i_a.text
