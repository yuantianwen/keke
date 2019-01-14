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
	sql="select a.sentenceid,a.zh,a.en,a.catid,ifnull(b.likeacount,0) as likeacount,ifnull(b.favorite,0) as favorite from t_content a left join t_like b on a.catid=b.catid and a.sentenceid=b.sentenceid and b.userid=1 where a.catid in (%s)"%(','.join(dict_catid.keys()))
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
		dict_sen["favorite"]=row[5]
		list_sen.append(dict_sen)
	return json.dumps(dict_cat)

def updateAndGetLikeAcount(catid,sentenceid,userid):
	likeacount = 1
	sql="select likeacount from t_like where userid=%s and catid =%s and sentenceid=%s"%(userid,catid,sentenceid)
	print(sql)
	cur = conn.execute(sql)
	row = cur.fetchone()
	if row == None:
		sql="insert INTO t_like(userid,catid,sentenceid,likeacount,favorite) values(%d,%d,%d,%d,0)"%(userid,catid,sentenceid,likeacount)
	else:	
		print(row[0])
		likeacount = row[0] + 1
		sql="update t_like set  likeacount =%d where userid=%d and catid=%d and sentenceid = %d"%(likeacount,userid,catid,sentenceid)
	#print(sql)

	conn.execute(sql)
	conn.commit()
	return(likeacount)


def updateAndGetFavorite(catid,sentenceid,userid):
	favorite = 1
	# 收藏
	sql="select favorite from t_like where userid=%s and catid =%s and sentenceid =%s"%(userid,catid,sentenceid)
	cur = conn.execute(sql)
	row = cur.fetchone()
	if row == None:
		sql="insert INTO t_like(userid,catid,sentenceid,likeacount,favorite) values(%d,%d,%d,0,%d)"%(userid,catid,sentenceid,favorite)
	else:
		if row[0]==0:
			favorite=1
		else:
			favorite=0
		sql="update t_like set  favorite =%d where userid=%d and catid=%d and sentenceid = %d"%(favorite,userid,catid,sentenceid)
	print(sql)
	conn.execute(sql)
	conn.commit()
	return(favorite)

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

