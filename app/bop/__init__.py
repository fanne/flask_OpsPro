# /usr/bin/python
#coding:utf-8

__Date__ = "2016-03-31 09:22"
__Author__ = 'eyu Fanne'

from flask import Blueprint

bop = Blueprint('bop',__name__)

from .import views