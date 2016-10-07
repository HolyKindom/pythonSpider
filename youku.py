#/usr/bin/python
#coding:utf-8

__Author__ = 'eyu Fanne'
__Date__ = '2016/7/24'

from bs4 import BeautifulSoup
import requests
import json
import sys
import re
reload(sys)
sys.setdefaultencoding('utf8')

heads={
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
"Accept-Encoding":"gzip, deflate, sdch",
"Accept-Language":"zh-CN,zh;q=0.8",
"Cache-Control":"max-age=0",
"Connection":"keep-alive",
"Host":"v.youku.com",
"Upgrade-Insecure-Requests":"1",
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
}


downUrl = r'http://v.youku.com/v_show/id_XMTU4Mjg2Njg4MA==.html?f=27312381'
youtubeUrl = r'https://www.youku.com'

myText = requests.get(downUrl,verify=False,headers=heads).text
mySoup = BeautifulSoup(myText,'lxml')
myComponent = mySoup.find_all(class_="m_component")
for i in myComponent:
    # print i
    print i.get('href')
# print myText