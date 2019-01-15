#!/usr/bin/python
#coding=utf-8
from flask_script import Manager

DBManager=Manager()

@DBManager.command
def init():
	print("数据库初始成功")

@DBManager.command
def migrate():
	print("数据库迁移成功")