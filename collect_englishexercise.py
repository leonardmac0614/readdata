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
import csv
import pytz
from dateutil import parser

def getTemplate():
   return '''---
title:  English exercise
date:   <title>
categories: 英语早操
thumbnail: http://p1.bpimg.com/567571/7720b01fba7e27d6.png
tags: English
photos:
- <picture>
---

"<content1>"
<p><content2></p>
'''
def getcontent(today):
	# today=str(datetime.datetime.now().strftime('%Y-%m-%d'))
    today = str(today)
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

def convert_date_to_num(enddate):
    a = datetime.datetime.strptime(str(datetime.datetime.now()).split(' ')[0],'%Y-%m-%d')
    date =datetime.datetime.strptime(enddate,'%Y-%m-%d')
    delta = (date - a).days
    return delta


def download(_url,name):#下载函数
    if(_url==None):#地址若为None则跳过
        pass
    result=urllib2.urlopen(_url)#打开链接
    #print result.getcode()
    if(result.getcode()!=200):#如果链接不正常，则跳过这个链接
        pass
    else:
        data=result.read()#否则开始下载到本地
        with open(name, "wb") as code:
            code.write(data)
            code.close()

def download_png(today):
    today = str(today)
    # today=str(datetime.datetime.now().strftime('%Y-%m-%d'))
    url = 'https://www.shanbay.com/soup/mobile/quote/'+today+'/?content_id=1676&social_service=x&url_key=8a60bd51c&content_type=quote%3Aquote&track_id=2696e460-11db-11e7-a294-00163e124371'
    try:
        request = urllib2.Request(url=url)
        response = urllib2.urlopen(request, timeout=20)
        result = response.read()
        html = BeautifulSoup(result,"html.parser")
        address = str(html.find_all('div',attrs={"class":"quote-preview"})[0]).split("(")[1].split("@")[0]
        print address
        if address !=None:
            pathName = "/Users/shuailong/Desktop/my_test/blog/readdata/image/" + today +".png"
            download(address,pathName)
    except:
        print today+"faild"
    # addres = link.get('data')

if __name__ == '__main__':
    
    today = datetime.date.today()
    enddate = "2017-06-30"

    num   = convert_date_to_num(enddate)

    for i in range(0,num,1):

        download_png(today)
        today = today + datetime.timedelta(days=1)
        print today
        print str(today)+" download success!"



    '''
    content_data     = []
    translation_data = []

    with open('names.csv','w') as csvfile:
        filedname = ['zn','cn']
        writer = csv.DictWriter(csvfile,filednames=filedname)
        writer.writeheader()


        for i in range(0,num,1):
            content_data.append(getcontent(today)[0])
            translation_data.append(getcontent(today)[1])
            writer.writerow({'zn':str(content_data.append(getcontent(today)[0])),'cn':'translation_data.append(getcontent(today)[1])'})
            # download_png(today)
            today = today + datetime.timedelta(days=1)
    print content_data,translation_data'''
