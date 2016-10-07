#coding:utf-8
#下载老学视频
from bs4 import BeautifulSoup
import requests
import configparser
import json
from json import JSONDecoder
import urllib
import multiprocessing
import os
import ctypes
import time
plays = ctypes.windll.kernel32

maizi_url = r'http://www.laoxue6699.cn/'
basedir = u'e:\各大网站视频教程'
CourseFrom = u'老学教育'



#print basedir
login_session = requests.session()
headers = {
            "Accept":"*/*",
            "Accept-Encoding":"gzip, deflate",
            "Accept-Language":"zh-CN,zh;q=0.8",
            "Connection":"keep-alive",
            "Content-Length":"51",
            "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
            "Host":"www.maiziedu.com",
            "Origin":"http://www.maiziedu.com",
            "Referer":"http://www.maiziedu.com/",
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36",
            "X-Requested-With":"XMLHttpRequest"
        }

headers_2 = {
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding":"gzip, deflate",
            "Accept-Language":"zh-CN,zh;q=0.8",
            "Cache-Control":"max-age=0",
            "Connection":"keep-alive",
            "Host":"www.maiziedu.com",
            "Referer":"http://www.maiziedu.com/course/list/",
            "Upgrade-Insecure-Requests":"1",
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36"
        }
class maiziEduLogin(object):
    def __init__(self,configfile):
        self.loginurl = r'http://www.laoxue6699.cn/login'

        config = configparser.ConfigParser()
        config.read(configfile)
        configname = 'maizi'
        self.username = config.get(configname,'account_l')
        self.password = config.get(configname,'password_l')


    def startLogin(self):
        #print self.username,self.password
        login_data = {
            'account_l':self.username,
            'password_l':self.password

        }
        s_login = login_session.post(self.loginurl,data=login_data,headers=headers)
        #print type(s_login)
        print s_login.status_code,s_login.text
        #print s_login.json()
        #print s_login.json()

def getVideoList():
    video_dict = {}
    pro_title = ''
    login = maiziEduLogin('config.ini')
    login.startLogin()


    my_url = r'http://www.maiziedu.com/course/380/'



    my_text = login_session.get(my_url,headers=headers_2).text
    my_soup = BeautifulSoup(my_text,'lxml')
    pro_title_list = my_soup.find("h1").text
    # print pro_title_list
    pro_title = pro_title.join(pro_title_list)
    pro_dir = basedir+'\\'+  CourseFrom +'\\' +pro_title
    print pro_dir
    if not os.path.exists(pro_dir):
        os.makedirs(pro_dir)
    video_name_list = my_soup.find(class_="lesson-lists")
    for i in video_name_list.find_all("a"):
        video_title = i.next_element.text
        video_url = maizi_url+i.get('href')
        # print video_url
        video_text = login_session.get(video_url,headers=headers_2).text
        video_soup = BeautifulSoup(video_text,'lxml')
        src = video_soup.find("source")
        mp4_url = src.get('src')  #下载视频的链接
        # print mp4_url
        # print video_title,u'%s' %mp4_url
        # video_dict[video_title] = mp4_url
        video_save = pro_dir + '\\' + video_title  #视频下载保存的路径
        video_dict[mp4_url] = video_save

    return video_dict

def startDownVideo(mp4_url,video_save):
    print '%s  %s.mp4' %(mp4_url,video_save)
    urllib.urlretrieve(u'%s' %mp4_url,'%s.mp4' %video_save)

def multiMan():
    pool = multiprocessing.Pool(processes=4)
    for k,v in getVideoList().items():
        pool.apply_async(startDownVideo,(k,v,))
    pool.close()
    pool.join()


if __name__=='__main__':
    multiMan()
    # getVideoList()
    # for i in range(5):
    #     time.sleep(1)
    #     plays.Beep(500,500)


