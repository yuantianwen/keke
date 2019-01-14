#!/usr/bin/python
#coding=utf-8
from flask  import Flask;
from flask import url_for,request,jsonify,abort
from db import getCatalogList,getContent,updateAndGetLikeAcount,updateAndGetFavorite

app = Flask(__name__)


@app.route("/")
def homepage():
	return app.send_static_file("index.html")

@app.route("/catalog",methods=['GET'])
def catalog():
	return catalog_list()

@app.route("/content",methods=['GET'])
def content():
	catname = request.args["catname"]
	sens=getContent(catname)
	return sens

@app.route("/like",methods=['GET','POST'])
def like():
	if request.method == 'GET':
		catid = request.args["catid"]
		userid = request.args["userid"]
		sentenceid = request.args["sentenceid"]
	elif request.method == 'POST':
		if request.mimetype=='application/json':
			catid=request.json["catid"]
			userid=request.json["userid"]
			sentenceid = request.json["sentenceid"]
		elif request.mimetype=='application/form':
			catid=request.form["catid"]
			userid=request.form["userid"]
			sentenceid=request.form["sentenceid"]
	likeacount= updateAndGetLikeAcount(catid,sentenceid,userid)
	return str(likeacount)

@app.route("/favorite",methods=['GET','POST'])
def favorite():
	if request.method == 'GET':
		catid = request.args["catid"]
		userid = request.args["userid"]
		sentenceid = request.args["sentenceid"]
	elif request.method == 'POST':
		if request.mimetype=='application/json':
			catid=request.json["catid"]
			userid=request.json["userid"]
			sentenceid = request.json["sentenceid"]
		elif request.mimetype=='application/form':
			catid=request.form["catid"]
			userid=request.form["userid"]
			sentenceid=request.form["sentenceid"]
	favorite= updateAndGetFavorite(catid,sentenceid,userid)
	return str(favorite)

# 获取目录列表
def catalog_list():
	str = getCatalogList()
	return str

# main http server 

def main():
	app.debug=True
	app.run(host="0.0.0.0",port=80)

if __name__ == '__main__':
	main()