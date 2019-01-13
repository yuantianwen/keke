#!/usr/bin/python
#coding=utf-8
import sqlite3;
import json

conn = 	sqlite3.connect("db/keke.db",check_same_thread=False)

def getCatalogList():
	global conn;
	catlist=[]

	sql = "select distinct catname from t_catalog"
	for row in conn.execute(sql):
		s = row[0]
		catlist.append(s)
	d={}
	d["catalogs"]=catlist
	return json.dumps(d)

def getContent(catname):
	dict_catid={}
	# ids=[]
	sql = "select id,subcatname from t_catalog where catname ='%s'"%catname
	for row in conn.execute(sql):
		# ids.append(str(row[0]))
		dict_catid[str(row[0])]=row[1]

	dict_cat={}
	sql="select a.sentenceid,a.zh,a.en,a.catid,ifnull(b.likeacount,0) as likeacount from t_content a left join t_like b on a.catid=b.catid and a.sentenceid=b.sentenceid and b.userid=1 where a.catid in (%s)"%(','.join(dict_catid.keys()))
	for row in conn.execute(sql):
		list_sen=[]
		subcatname = dict_catid[str(row[3])]
		if dict_cat.has_key(subcatname):
			list_sen=dict_cat[subcatname]
		else:
			dict_cat[subcatname]=list_sen
		dict_sen={}
		dict_sen["sentenceid"]=row[0]
		dict_sen["zh"]=row[1]
		dict_sen["en"]=row[2]
		dict_sen["catid"]=row[3]
		dict_sen["likeacount"]=row[4]
		list_sen.append(dict_sen)
	return json.dumps(dict_cat)

def updateAndGetLikeAcount(catid,sentenceid,userid):
	likeacount = 0
	sql="select likeacount from t_like where userid=%s and catid =%s and sentenceid =%s"%(userid,catid,sentenceid)
	
	cur = conn.execute(sql)
	row = cur.fetchone()
	if row != None:	
		likeacount = row[0]
	print(likeacount)

	# 点赞加1
	likeacount +=1
	sql="REPLACE INTO t_like(userid,catid,sentenceid,likeacount) values(%d,%d,%d,%d)"%(userid,catid,sentenceid,likeacount)
	print(sql)
	conn.execute(sql)
	conn.commit()
	return(likeacount)

def db_close():
	global conn;
	if not conn == None:
		conn.close()


if __name__ == '__main__':
	print getContent('旅游计划')
	# d = eval(getCatalogList())

	# cat = d["catalogs"]
	# print cat
	#l = eval(cat)
	#print(type(l[1]))
