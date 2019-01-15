#!/usr/bin/python
#coding=utf-8
import sqlite3
import io,re

conn = 	sqlite3.connect("db/keke.db")

def getCatalogID(theme,subtheme):
	global conn;
	sql = "select id from t_catalog where catname=\"%s\" and subcatname=\"%s\""%(theme,subtheme)
	cur = conn.execute(sql)
	str = cur.fetchone()
	return int(str[0])

id = 0;
catid=0;
sen_zh="";
sen_en="";
line_type=""

with io.open('keke.txt','r',encoding="utf-8") as f:
	for str in f.readlines():
		str = str.replace('\n','')
		if str=="":
			continue
		if str.startswith(u'旅游英语口语就该这么说'):
			new_segment_flag = 1;
			#newfile.write(segment)
			idx = "";
			theme=""
			subtheme=""
			s = str.split(' ')
			#print(s)
			searchobj = re.search(u'.*第(\d+)期.*',s[0])
			if searchobj:
				idx = searchobj.group(1)
			if len(s) <=2:
				theme = s[1]
			else:
				theme = s[1]
				subtheme=s[2]
			line_type="zh"
			id=0
			sen_zh=""
			sen_en=""
			catid = getCatalogID(theme,subtheme)
			#segment="[第%s期,%s,%s]"%(idx,theme,subtheme)		
		else:
			new_segment_flag = 0;

			if line_type=='zh':
				sen_zh = str				
				line_type='en'
			elif line_type=='en':
				line_type="zh"
				sen_en = str
				id+=1
				sql = "insert into t_content(catid,sentenceid,zh,en) values(?,?,?,?)"
				conn.execute(sql,[catid,id,sen_en,sen_zh])
				sen_zh=""
				sen_en=""
				
	conn.commit()

print("hello")