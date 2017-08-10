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

def get_image():
    # https://alpha.wallhaven.cc/random?page=5
    yesterday = ("").join(str(datetime.date.today()-datetime.timedelta(days=1)).split("-"))
    # url = "http://www.istartedsomething.com/bingimages/#"+yesterday+"-gb"
    # print url
    url = "https://alpha.wallhaven.cc/"
    print url
    request = urllib2.Request(url=url)
    request.add_header("User-agent", "Mozilla 5.10")
    response = urllib2.urlopen(request, timeout=20)
    result = response.read()
    print result
    exit()
    html = BeautifulSoup(result,"html.parser")
    try:
		content= html.find_all('p',attrs={"class": "content"})[0]
		content = content.get_text()
    except:
		pass

    return link

if __name__ == '__main__':
    get_image()
