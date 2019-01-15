#!/usr/bin/python
#coding=utf-8
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# 定义配置基类
class Config:
	# 主机和端口
	HOST="127.0.0.1"
	PORT=80
	# 秘钥

	# 自动提交

	# 发邮件 配置

	#文件上传的位置

	# 额外的初始化操作
	@staticmethod
	def init_app(app):
		pass

class DevelopConfig(Config):
	SQLITE_DATABASE_URI="db/keke.db"

class TestConfig(Config):
	SQLITE_DATABASE_URI="db/keke.db"

class ProductConfig(Config):
	SQLITE_DATABASE_URI="db/keke.db"

config = {
	'default':DevelopConfig,
	'develop':DevelopConfig,
	'test':TestConfig,
	'product':ProductConfig
},
		