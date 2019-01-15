#!/usr/bin/python
#coding=utf-8

from app import create_app
from flask_script import Manager
import os
# 从环境变量中获取config_name
config_name = os.environ.get('FLASK_CONFIG') or 'default'

# 生成app
app = create_app(config_name)

manager = Manager(app)

# 启动manager
if __name__ == '__main__':
	manager.run()
