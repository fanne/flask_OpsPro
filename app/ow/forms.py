# /usr/bin/python
#coding:utf-8

__Date__ = "2016-03-26 15:32"
__Author__ = 'eyu Fanne'

from flask_wtf import Form
from wtforms import IntegerField,StringField,SubmitField
from wtforms.validators import DataRequired,Required

class OwGameForm(Form):
    id = IntegerField('OwGameServer Id',[DataRequired()])
    name = StringField('OwGameServer Name',[DataRequired()])
    host = StringField('OwGameServer Host',[DataRequired()])
    port = StringField('OwGameServer Port',[DataRequired()])

class CommandForm(Form):
    command = StringField('Command SQl',[DataRequired()])
    # submit = SubmitField('Submit')

class VersionForm(Form):
    version = IntegerField('Version Num',[DataRequired()])

class PatchCommandForm(Form):
    patchcommand = StringField('Patch Command',[DataRequired()])
