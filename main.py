#!/usr/bin/python
#coding=utf-8
from urllib import request
from bs4 import BeautifulSoup
import bs4

import re,io,sys
import chardet


import requests

ua_headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}

save_file="旅游英语口语就该这么说.txt"
f = open(save_file,'w')


def parse_one_theme(url):
	print("begin parse url:%s"%(url))
	req = request.Request(url=url,headers=ua_headers)
	res = request.urlopen(req)
	data = res.read()#.decode('ISO-8859-1')
	data = data.decode('utf-8')

	soup = BeautifulSoup(data,"lxml")
	list = soup.select(".info-qh")
	for info in list:
		'''
		for child in info.children:
			if 	type(child)==bs4.element.Tag:
				#print(type(child.get('class')))
				if child.get('class')[0] == 'qh_en':
					print(child.text)
				elif child.get('class')[0] == 'qh_zg':
					print(child.text)
		'''
		f.write(info.text)

def main():
	# 准备所有网址
	url_list=["http://www.kekenet.com/kouyu/17090/List_%s.shtml"%(i) for i in range(1,20)]
	url_list.append("http://www.kekenet.com/kouyu/17090/")
	
	# 遍历网址
	for url in url_list:
		#url = "http://www.kekenet.com/kouyu/17090/List_%s.shtml"%(i)
		#url="http://www.kekenet.com/kouyu/17090/"
		print("start download",url)
		req = request.Request(url=url,headers=ua_headers)

		response = request.urlopen(req)
		html = response.read()
		soup = BeautifulSoup(html,"lxml")
		list = soup.find_all(title=re.compile("旅游英语口语就该这么说.*"))
		#list = soup.find_all(text='旅游英语口语就该这么说(MP3+字幕):第6期 旅游计划 去多久')
		#list = soup.find_all(target="_blank")
		for x in list:
			f.write("\r\n"+x.text)
			parse_one_theme(x.get('href'))
			#parse_one_theme(BeautifulSoup(x,"lxml").href)
		
	f.close()
if __name__ == '__main__':
	main()
