# /usr/bin/python
#coding:utf-8

__Date__ = "2016-07-01 16:07"
__Author__ = 'eyu Fanne'


from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class PatchCommandForm(Form):
    patchcommand = StringField('Patch Command',[DataRequired()])
