# /usr/bin/python
#coding:utf-8

__Date__ = "2016-03-26 13:39"
__Author__ = 'eyu Fanne'

from .import db

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True)

    def __repr__(self):
        return '<Role %r>' %self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64),unique=True,index=True)

    def __repr__(self):
        return '<User %r>' %self.username

class OwGame(db.Model):
    __tablename__ = 'OwGames'
    serverId = db.Column(db.Integer,primary_key=True)
    serverName = db.Column(db.String(32),unique=True,index=True)
    serverHost = db.Column(db.String(64),index=True)
    serverPort = db.Column(db.Integer)

    def __repr__(self):
        return '%s' %self.serverHost

class BopGame(db.Model):
    __tablename__ = 'BopGames'
    serverId = db.Column(db.Integer,primary_key=True)
    serverName = db.Column(db.String(32),unique=True,index=True)
    serverHost = db.Column(db.String(64),unique=True,index=True)

    def __repr__(self):
        return '%s' %self.serverHost

class OwGlobal(db.Model):
    __tablename__ = 'OwGlobals'
    serverId = db.Column(db.Integer,primary_key=True)
    serverName = db.Column(db.String(32),unique=True,index=True)
    serverHost = db.Column(db.String(64),unique=True,index=True)
    serverPort = db.Column(db.Integer)

    def __repr__(self):
        return '%s' %self.serverHost

class OwCross(db.Model):
    __tablename__ = 'OwCross'
    serverId = db.Column(db.Integer,primary_key=True)
    serverName = db.Column(db.String(32),unique=True,index=True)
    serverHost = db.Column(db.String(64),unique=True,index=True)
    serverPort = db.Column(db.Integer)

    def __repr__(self):
        return '%s' %self.serverHost