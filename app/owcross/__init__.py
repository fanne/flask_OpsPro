# /usr/bin/python
#coding:utf-8

__Date__ = "2016-07-21 17:07"
__Author__ = 'eyu Fanne'

from flask import Blueprint

owcross = Blueprint('owcross',__name__)

from .import views