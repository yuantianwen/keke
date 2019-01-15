#!/usr/bin/python
#coding=utf-8

from flask import Blueprint

main = Blueprint('main',__name__)

@main.route("/")
def homepage():
	return areturn render_template('common/index.html')