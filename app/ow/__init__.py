# /usr/bin/python
#coding:utf-8

__Date__ = "2016-03-31 10:12"
__Author__ = 'eyu Fanne'

from flask import Blueprint

ow = Blueprint('ow',__name__)

from .import views