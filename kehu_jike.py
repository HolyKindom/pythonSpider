#/usr/bin/python
#coding:utf-8

__Author__ = 'eyu Fanne'
__Date__ = '2016/6/5'

#-*-coding:utf8-*-
import requests
import re
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class spider(object):
    def __init__(self):
        print u'开始爬取内容。。。'
    def getsource(self,url):
        html = requests.get(url)
        return html.text
    def changepage(self,url,total_page):
        # now_page = int(re.seach('pageNum=(\d+)',url,re.S).group(1))
        print total_page
        print type(total_page)
        print 'ddddddddddd'
        page_group = []
        for i in range(1,total_page+1):
            # print i
            link = re.sub('pageNum=\d+','pageNum=%s'%i,url,re.S)
            print link
            page_group.append(link)
        return page_group
    def geteveryclass(self,source):
        everyclass = re.findall('<div class="lessonimg-box">(.*?)<li id="',source,re.S)
        print everyclass
        return everyclass
    def getinfo(self,eachclass):
        info = {}
        info['title'] = re.search('class="lessonimg" title="(.*?)" alt="',eachclass,re.S).group(1)
        print info['title']
        info['content'] = re.search('</h2><p>(.*?)</p>',eachclass,re.S).group(1)
        info['classlevel'] = re.search('<i class="xinhao-icon3"></i><em>(.*?)</em>',eachclass,re.S).group(1)
        info['learnnum'] = re.search('<em class="learn-number">(.*?)</em>',eachclass,re.S).group(1)
        print info
        return info
    def saveinfo(self,classinfo):
        f = open('info.txt','a')
        for each in classinfo:
            f.writelines('title:'+each['title'] + '\n')
            f.writelines('content:' + each['content'] + '\n')
            f.writelines('classlevel:' + each['classlevel'] + '\n')
            f.writelines('learnnum:' + each['learnnum' + '\n\n'])
        f.close()


if __name__=='__main__':
    print 'ssssss'

    classinfo = []
    url = 'http://www.jikexueyuan.com/course/?pageNum=1'
    print url
    jikespider = spider()
    # jikespider.changepage(url,20)
    all_links =jikespider.changepage(url,20)
    print 'all_links is %s' %all_links
    for link in all_links:
        print u'正在处理页面：' + link
        html = jikespider.getsource(link)
        print html
    #     everyclass = jikespider.geteveryclass(html)
    #     for each in everyclass:
    #         info = jikespider.getinfo(each)
    #         classinfo.append(info)
    # jikespider.saveinfo(classinfo)



