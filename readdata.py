#!/usr/bin/python
#coding:utf-8
import sys
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

import os
from os import listdir
from os.path import isfile, join 
from datetime import datetime
import numpy as np
import pandas as pd
import xlrd 
import xlwt 
import os
import time
import calendar
import pytz
import json
import urllib
import urllib2
global excels
global excels_name 
	
def readexcel(directory):
	filenames = list()
	for i in os.walk(directory):
		for j in i:
			filenames += [k for k in j if k.endswith(".xlsx")]
	return filenames


def read_english(directory):
	da = xlrd.open_workbook("english.xlsx")
	sh = da.sheet_by_index(0)
	delta = convert_date_to_num()[1]

	a = datetime.now().strftime("%Y-%m-%d")

	en = sh.col_values(0)[2*(delta-1)].split(".")[1]
	print sh.col_values(0)[2*(delta-1)]
	cn = sh.col_values(0)[2*(delta-1)+1]
	tpl = getTemplate()

	tpl = tpl.replace("<title>",a)
	tpl = tpl.replace("<content1>",en)
	tpl = tpl.replace("<content2>",cn)

	return tpl,a,delta


def convert_date_to_num():
	a = datetime.now()
	date = datetime.strptime("2017-01-10", "%Y-%m-%d") 
	delta =  (a-date).days
	return a,delta


def getTemplate():
   return '''---
layout: post
title:  "英语早操"
date:   <title>
categories: English
author:     "leonardmac"
header-img: "img/home-bg.jpg"
tags:
    - 英语
---

<content1>
<p><content2></p>

<p>{{ page.date | date_to_string }}</p>

<!-- more -->
> #### 打赏:  &nbsp;[*戳这里*](http://leonardmac.me/Donate/)
'''

		



files = read_english(".")[0]
date = read_english(".")[1]
delta = str(read_english(".")[2])
print files,date

w = open(date +"-English-exercise-"+ delta +'day.md','w')
w.write(files)
w.close()
exit()
with open('date'+"Enlish exercise-"+delta+'days.md','w') as w:
	w.write(files)


print files,date













