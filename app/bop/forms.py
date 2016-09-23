# /usr/bin/python
#coding:utf-8

__Date__ = "2016-03-26 15:32"
__Author__ = 'eyu Fanne'

from flask_wtf import Form
from wtforms import IntegerField,StringField,SubmitField
from wtforms.validators import DataRequired,Required

class BopGameForm(Form):
    id = IntegerField('BopGameServer Id',[DataRequired()])
    name = StringField('BopGameServer Name',[DataRequired()])
    host = StringField('BopGameServer Host',[DataRequired()])

class CommandForm(Form):
    command = StringField('Command SQl',[DataRequired()])

class VersionForm(Form):
    version = IntegerField('Version Num',[DataRequired()])
