#!/usr/bin/python
#coding=utf-8
from flask  import Flask,render_template;
from app.config import config

def config_errorhandler(app):
	# 如果在蓝本定制，则只针对蓝本的错误有效。
	# 可以使用app_errorhandler定制全局有效的错误显示
	# 定制全局404错误页面
	@app.errorhandler(404)
	def page_not_found(e):
		return render_template('error/404.html',e=e)
# 将创建app的动作封装成一个函数
def create_app(config_name):
	# 创建app实例对象
	app = Flask(__name__)
	# 加载配置

	# 执行额外的初始化

	#设置debug=True,让toolbar生效
	# app.debug=True

	# 配置蓝本
	config_blueprint(app)
	# 配置全局错误处理
	config_errorhandler(app)

	# 返回app实例对象
	return app