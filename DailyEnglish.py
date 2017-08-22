#!/usr/bin/env python
# coding:utf8

import sys
reload(sys)
sys.setdefaultencoding("utf8")

# 加载库
import urllib
import urllib2
import json
from bs4 import BeautifulSoup
import datetime
import os
import time
import commands
import traceback

# log.startLogging(open("/Users/shuailong/Desktop/my_test/blog/readdata/deploy.log",'w'))

def getTemplate():
   return '''---
title:  English exercise
date:   <title>
categories: 英语早操
thumbnail: <url1>
tags: English
photos:
- <url2>
---

"<content1>"
<p><content2></p>
'''
def getcontent():
	today=str(datetime.datetime.now().strftime('%Y-%m-%d'))
    # https://www.shanbay.com/soup/mobile/quote/2017-05-08/?content_id=1676&social_service=x&url_key=8a60bd51c&content_type=quote%3Aquote&track_id=2696e460-11db-11e7-a294-00163e124371
	url = 'https://www.shanbay.com/soup/mobile/quote/'+today+'/?content_id=1676&social_service=x&url_key=8a60bd51c&content_type=quote%3Aquote&track_id=2696e460-11db-11e7-a294-00163e124371'
	request = urllib2.Request(url=url)
	response = urllib2.urlopen(request, timeout=20)
	result = response.read()
	html = BeautifulSoup(result,"html.parser")

	try:
		content= html.find_all('div',attrs={"class": "content"})[0]
		content = content.get_text()

	except:
		pass

	try:
		translation = html.find_all('div',attrs={"class": "translation"})[0]
		translation = translation.get_text()

	except:
		pass


	return content,translation

def convert_date_to_num():
	a = datetime.datetime.now()
	b =str(a)
	date = datetime.datetime.strptime("2017-01-20", "%Y-%m-%d")
	delta =  (a-date).days
	return b,delta

def get_image():
    # http://www.istartedsomething.com/bingimages/?m=5&y=2017#20170620-us
    yesterday = ("").join(str(datetime.date.today()-datetime.timedelta(days=1)).split("-"))

    url = "http://www.istartedsomething.com/bingimages/#"+yesterday+"-gb"
    # print url
    request = urllib2.Request(url=url)
    response = urllib2.urlopen(request, timeout=20)
    result = response.read()
    html = BeautifulSoup(result,"html.parser")
    try:
		content= html.find_all('p',attrs={"class": "content"})[0]
		content = content.get_text()
    except:
		pass

    return link
if __name__ == '__main__':

    import random
    num = str(int(random.uniform(1,500000)))
    url = "https://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-"+num+".jpg"

    files = getTemplate()
    content = getcontent()[0]
    translation = getcontent()[1]
    date = str(datetime.datetime.now().strftime('%Y-%m-%d'))
    delta = str(convert_date_to_num()[1])

    files = files.replace("<title>",date)
    files = files.replace("<content1>",content)
    files = files.replace("<content2>",translation)
    files = files.replace("<url1>",url)
    files = files.replace("<url2>",url)
    # url = get_image()
    # files = files.replace("<url1>",url)
    # files = files.replace("<url2>",url)



    w = open(date +"-English-exercise-"+ delta +'day.md','w')
    w.write(files)
    w.close()
    print "create new post"

    terminal = "mv "+ date +"-English-exercise-"+ delta +"day.md ../hexo_test/source/_posts"
    os.system(terminal)
    os.chdir("/root/hexo_test")
    generate = "hexo generate"
    deploy = "hexo deploy"

    try:
		os.system(generate)
    except:
		print "hexo generate error"
    print "generate"

    time.sleep(20)
    try:
		os.system(deploy)
		print "well done!"
    except:
		print "hexo deploy error"
