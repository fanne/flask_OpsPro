# /usr/bin/python
#coding:utf-8

__Date__ = "2016-03-31 09:23"
__Author__ = 'eyu Fanne'


from .import bop
from flask import render_template,redirect,url_for,flash,session,request,current_app
from .forms import BopGameForm,CommandForm,VersionForm
from ..import db
from ..models import BopGame
from sqlselect import runSql
from bopinfo import pronameDict,proDic
from bopsync import startRsync
import collections


@bop.route('/bopsql',methods=['GET','POST'])
def bopsql():
    cmdsql = None
    commandform = CommandForm()
    serverlists = BopGame.query.all()

    if commandform.validate_on_submit():
        session['cmdsql'] = commandform.command.data
        session['serverID'] = request.form.getlist('dbcheckbox')

        #判断是否选服
        if session.get('serverID') == []:
            flash(u'未选游戏服,请勾选游戏服!')
            return redirect(url_for('bop.bopsql'))

        session['indexsql'] = {}
        for db in session.get('serverID'):
            dbsql = BopGame.query.filter_by(serverId=db).first()
            dbhost = dbsql.serverHost
            dbname = dbsql.serverName
            session['dbname'] = dbname
            session['sqlres'] = runSql(dbhost=dbhost,serverid=db,sql=session.get('cmdsql'))
            session.get('indexsql')[db] = session.get('sqlres')
        flash(u'查询数据库完成')
        session['sqldic'] = collections.OrderedDict(sorted(session.get('indexsql').items(),key=lambda t:t[0]))
        return redirect(url_for('bop.bopsql'))
    return render_template('bop/bopsql.html',
                           commandform=commandform,
                           cmdsql=session.get('cmdsql'),
                           serverlists=serverlists,
                           dbname = session.get('dbname'),
                           sqldic = session.get('sqldic')
                           )

@bop.route('/bopRedis',methods=['GET','POST'])
def bopRedis():
    return render_template('bop/bopRedis.html')


@bop.route('/addBop',methods=['GET','POST'])
def addBop():
    bopserverform = BopGameForm()
    if bopserverform.validate_on_submit():
        gameserver = BopGame.query.filter_by(serverId=bopserverform.id.data).first()
        if gameserver is None:
            gameserver = BopGame(serverId=bopserverform.id.data,
                                serverName=bopserverform.name.data,
                                serverHost=bopserverform.host.data)
            db.session.add(gameserver)
            db.session.commit()
            flash('add server complete')
            return redirect(url_for('bop.addBop'))
        else:
            flash('serverId is exits')
            return redirect(url_for('bop.addBop'))
    else:
        print 'run out'
    return render_template('bop/addBop.html',bopserverform=bopserverform)




@bop.route('/updateBop',methods=['GET','POST'])
def updateBop():
    versionform = VersionForm()
    if versionform.validate_on_submit():
        session['proId'] = request.form.get('selectid')
        session['versionNum'] = versionform.version.data
        proId = session.get('proId')
        versionNum = session.get('versionNum')
        app = current_app._get_current_object()
        startRsync(app,proDic,proId,versionNum)
        return redirect(url_for('bop.updateBop'))
    return render_template('bop/updateBop.html',
                           prodict = pronameDict(),
                           versionform = versionform)

@bop.route('/PatchBop',methods=['GET','POST'])
def PatchBop():
    serverlists = BopGame.query.all()
    return render_template('bop/patchBop.html',
                           serverlists=serverlists)
