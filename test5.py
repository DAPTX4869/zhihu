#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-01 16:36:29
# @Author  : ${DAPTX} (${DAPTX4869@foxmail.com})
# @Link    : http://example.org
# @Version : $Id$

import os
import urllib.request
from bs4 import BeautifulSoup
import re
import time

url = 'http://www.hrb6.com/hrb6/15/15103/'
link= '3798930.html'
i=1
while True:
	f = urllib.request.urlopen(url+link)
	string = f.read().decode('ANSI','replace')
	Smain=BeautifulSoup(string,'html5lib').find('div',{'id':'novel_content'})
	writing=BeautifulSoup(str(Smain), 'html5lib').get_text()

	st=BeautifulSoup(string,'html5lib').find('h1',{'class':'novel_title'})
	title=BeautifulSoup(str(st), 'html5lib').get_text()


	la=BeautifulSoup(string,'html5lib').find('div',{'class':'novel_bottom'})
	las=BeautifulSoup(str(la), 'html5lib').find_all('a')
	last = BeautifulSoup(str(las), 'html5lib').get_text()
	link = las[2].get('href')
	
	ebook=open("book.txt","a+",encoding='utf-8')
	if last[13]=="二":
		ebook.write('\n\n')
		ebook.write(title)
		ebook.write('\n\n')
	ebook.write(writing)
	# ebook.write('\n\n')
	ebook.close()

	print("第",i,"章写入成功")
	
	i+=1
	time.sleep(1)
	if link == '3799268.html':
		print('over')
		break
		


