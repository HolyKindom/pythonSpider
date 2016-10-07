#coding:utf-8
#下载慕课网的视频 早期视频

from bs4 import BeautifulSoup
import requests
import configparser
import json
from json import JSONDecoder
import urllib
import multiprocessing
import os

urlopen = urllib.URLopener()
imooc_url = r'http://www.imooc.com'
basedir = u'D:\各大网站视频教程'
# basedir = os.path.abspath('.')
CourseFrom = u'慕课网'
login_session = requests.session()
headers = {
            "Accept":"application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding":"gzip, deflate",
            "Accept-Language":"zh-CN,zh;q=0.8",
            "Connection":"keep-alive",
            "Host":"www.imooc.com",
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36",
            "X-Requested-With":"XMLHttpRequest"
        }


class imoocLogin(object):
    def __init__(self,configfile):
        self.loginurl = r'http://www.imooc.com/passport/user/login'

        config = configparser.ConfigParser()
        config.read(configfile)
        configname = 'imooc'
        self.username = config.get(configname,'username')
        self.password = config.get(configname,'password')


    def startLogin(self): #执行登入操作
        login_text = requests.get(imooc_url).text
        login_soup = BeautifulSoup(login_text,'lxml')
        verify = login_soup.find_all('img',class_="verify-img")
        #print "verify: %s" %verify
        if verify:
            for verify_data in verify:
                verify_data = verify_data.get('src')
                verify_url = imooc_url+verify_data
                # print verify_url
                verify_data = raw_input('input verify:')
                login_data = {
                    "username":self.username,
                    "password":self.password,
                    "remember":'1',
                    "verify":verify_data,
                    "referer":"http://www.imooc.com"
                }
        else:
            login_data = {
                "username":self.username,
                "password":self.password,
                "remember":"1",
                "referer":"http://www.imooc.com"
            }
        s_login = login_session.post(self.loginurl,data=login_data,headers=headers)
        # print(s_login)
        # print s_login.json()
        # print type(s_login.json())
        # for k,v in s_login.json().items():
        #     print k,v

def getVideoList():
    video_dict = {}
    imooc_url = r'http://www.imooc.com'
    #url_in = raw_input('input url:')
    #url_text = requests.get(url_in).text
    url_text = requests.get(r'http://www.imooc.com/view/37').text
    url_soup = BeautifulSoup(url_text,'lxml')
    print url_soup
    pro_title = url_soup.h2.text
    print pro_title
    #print url_soup
    video_urls = url_soup.find_all(class_="J-media-item studyvideo")
    print video_urls
    pro_dir = basedir+'\\'+  CourseFrom +'\\' +pro_title
    print pro_dir
    if not os.path.exists(pro_dir):
        os.makedirs(pro_dir)
    for video_i in video_urls:
        j = ''
        video_url = imooc_url + video_i.get('href')
        print video_url
        video_title = video_i.text.strip().split()
        video_title = j.join(video_title[0:-1])
        #print video_title
        video_id = video_i.get('href').split(r'/')[-1]
        bac_url = r'http://www.imooc.com/course/ajaxmediainfo/?mid=%s&mode=flash' %video_id
        loginPro = imoocLogin('config.ini')
        loginPro.startLogin()
        video_url = login_session.get(bac_url,headers=headers).text
        video_soup = BeautifulSoup(video_url,'lxml')
        video_str = video_soup.get_text().encode('utf-8')
        video_json = json.loads(video_str)
        video_down_url = video_json['data']['result']['mpath'][2]
        print video_title,video_down_url
        video_save = pro_dir + '\\' + video_title  #视频下载保存的路径
        video_dict[video_save] = video_down_url
        try:
            pass
            # urllib.urlretrieve(video_down_url,'%s.mp4' %video_save)
        except Exception,e:
            print Exception,":",e
            print '%s is error url' %video_title

    #return video_dict

def startDownVideo(url,title):
    print '%s,%s' %(title,url)
    #urllib.urlretrieve(url,'%s.mp4' %title)

def multiMan():
    pool = multiprocessing.Pool(processes=4)
    for k,v in getVideoList().items():
        pool.apply_async(startDownVideo,(k,v,))
    pool.close()
    pool.join()



if __name__=='__main__':
    getVideoList()
    #multiMan()






