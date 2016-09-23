# /usr/bin/python
#coding:utf-8

__Date__ = "2016-03-25 17:54"
__Author__ = 'eyu Fanne'

from flask import render_template,flash,redirect,url_for,request,session

from .import main
from ..import db
from ..models import BopGame,OwGame
from app.ow.sqlselect import runSql


@main.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')


@main.route('/initserver',methods=['GET','POST'])
def initserver():
    return render_template('initserver.html')



@main.route('/products/<product>/',methods=['GET','POST'])
def products(product):
    return render_template('%s.html' %product, msg='Buy our {}'.format(product))


@main.route('/getdata',methods=['GET','POST'])
def getdata():
    owLists = OwGame.query.all()
    bopLists = BopGame.query.all()
    return render_template('getdata.html',owLists=owLists,bopLists=bopLists)



