# /usr/bin/python
#coding:utf-8

__Date__ = "2016-03-25 19:32"
__Author__ = 'eyu Fanne'

from flask import render_template
from .import main

@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@main.app_errorhandler(500)
def page_not_found(e):
    return render_template('500.html'),500
