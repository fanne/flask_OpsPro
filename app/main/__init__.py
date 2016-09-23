# /usr/bin/python
#coding:utf-8

__Date__ = "2016-03-25 19:03"
__Author__ = 'eyu Fanne'

from flask import Blueprint

main = Blueprint('main',__name__)

from .import views,errors
