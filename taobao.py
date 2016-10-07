# /usr/bin/python
#coding:utf-8

__Date__ = "2016-09-21 12:42"
__Author__ = 'eyu Fanne'

##爬取淘宝价格
import requests
from bs4 import BeautifulSoup
import json
import re

headers={
    ":authority":"s.taobao.com",
    ":method":"GET",
    ":path":"/api?_ksTS=1474433321832_242&callback=jsonp243&ajax=true&m=customized&rn=6389ba4fef60ba2cb7b24db572a94f31&initiative_id=tbindexz_20160921&ie=utf8&spm=a21bo.50862.201856-taobao-item.2&sourceId=tb.index&search_type=item&ssid=s5-e&commend=all&imgfile=&q=%E7%A1%AC%E7%9B%98&suggest=history_1&_input_charset=utf-8&wq=&suggest_query=&source=suggest&s=36&bcoffset=-1",
    ":scheme":"https",
    "accept":"text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",
    "accept-encoding":"gzip, deflate, sdch, br",
    "accept-language":"zh-CN,zh;q=0.8",
    "cache-control":"max-age=0",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36",
    "x-requested-with":"XMLHttpRequest",
}


taobao_url = r'https://s.taobao.com/api?_ksTS=1474433321832_242&callback=jsonp243&ajax=true&m=customized&rn=6389ba4fef60ba2cb7b24db572a94f31&initiative_id=tbindexz_20160921&ie=utf8&spm=a21bo.50862.201856-taobao-item.2&sourceId=tb.index&search_type=item&ssid=s5-e&commend=all&imgfile=&q=%E7%A1%AC%E7%9B%98&suggest=history_1&_input_charset=utf-8&wq=&suggest_query=&source=suggest&s=36&bcoffset=-1'
taobao_data = requests.get(taobao_url,headers=headers).text
print taobao_data
taobao_json = re.findall("\{.*\}",taobao_data)
# print taobao_json

for i in taobao_json:
    print type(i)
