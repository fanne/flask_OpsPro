# /usr/bin/python
#coding:utf-8

__Date__ = "2016-07-21 17:10"
__Author__ = 'eyu Fanne'

from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired


class CommandForm(Form):
    command = StringField('Command SQl',[DataRequired()])

class PatchCommandForm(Form):
    patchcommand = StringField('Patch Command',[DataRequired()])