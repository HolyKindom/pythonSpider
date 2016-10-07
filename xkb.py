# /usr/bin/python
#coding:utf-8

__Date__ = "2016-09-21 09:20"
__Author__ = 'eyu Fanne'

###爬取新华快报内容

import requests
from bs4 import BeautifulSoup
import json

xhb_url = r'http://epaper.xkb.com.cn/'
request_url = r'http://epaper.xkb.com.cn/index.php'

headers = {
            "Accept":"*/*",
            "Accept-Encoding":"gzip, deflate",
            "Accept-Language":"zh-CN,zh;q=0.8",
            "Connection":"keep-alive",
            "Content-Length":"17",
            "Content-Type":"application/x-www-form-urlencoded",
            "Host":"epaper.xkb.com.cn",
            "Origin":"http://epaper.xkb.com.cn",
            "Referer":"http://epaper.xkb.com.cn/",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36",
            "X-Requested-With":"XMLHttpRequest"
        }

post_data = {
    "act":"img",
    "id":258013,
}

get_session = requests.session()

get_data = get_session.post(request_url,data=post_data,headers=headers)

print get_data.status_code,get_data.text
data_json = get_data.json()
print type(data_json)

print json.dumps(data_json,indent=4)
# soup_file = BeautifulSoup(get_data.text,'lxml')