# /usr/bin/python
#coding:utf-8

__Date__ = "2016-07-20 10:45"
__Author__ = 'eyu Fanne'


from bs4 import BeautifulSoup
import requests
import json
import sys
import re
reload(sys)
sys.setdefaultencoding('utf8')


downUrl = r'https://www.youtube.com/playlist?list=PLXO45tsB95cKKyC45gatc8wEc3Ue7BlI4'
youtubeUrl = r'https://www.youtube.com'

myText = requests.get(downUrl,verify=False).text

myStr = myText.encode("utf-8")

myList = re.findall("\/watch\?v=.*;index=\d",myStr)
for i in myList:
    print "%s%s" %(youtubeUrl,i)
