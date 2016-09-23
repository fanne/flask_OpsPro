# /usr/bin/python
#coding:utf-8

__Date__ = "2016-07-01 16:04"
__Author__ = 'eyu Fanne'
from flask import Blueprint

owglobal = Blueprint('owglobal',__name__)

from .import views
