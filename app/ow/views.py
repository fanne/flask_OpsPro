# /usr/bin/python
#coding:utf-8

__Date__ = "2016-03-31 10:12"
__Author__ = 'eyu Fanne'

from flask import render_template,flash,redirect,url_for,request,session,current_app
from .import ow
from ..models import OwGame
from forms import OwGameForm,CommandForm,VersionForm,PatchCommandForm
from ..import db
from app.ow.sqlselect import runSql
from owinfo import pronameDict,proDic
from owrsync import startRsync
from owpatch import startPatch
from addServerToStart import ThreadAddServer
import collections
import os
import re
import time
from os import path
from app import create_app
from werkzeug.utils import secure_filename
from app.common.myLogConfig import logConfig
from subprocess import PIPE,Popen,STDOUT

app = create_app('default')
upload_path = app.config['UPLOAD_FOLDER']
if not os.path.exists(upload_path):
    os.mkdir(upload_path)


warning_command = ['init','stop','start','restart','kill',';','&&','root','tmp','global','Global','owglobal']
allow_command = ['patch','com.my9yu.h5game.modules.patch']
patch_logfile = app.config['PATCH_LOGFILE']
ansible_host_file = '/etc/ansible/hosts'




@ow.route('/owsql',methods=['GET','POST'])
def owsql():
    cmdsql = None
    commandform = CommandForm()
    serverlists = OwGame.query.all()

    if commandform.validate_on_submit():
        session['cmdsql'] = commandform.command.data
        session['serverID'] = request.form.getlist('dbcheckbox')

        #判断是否选服
        if session.get('serverID') == []:
            flash(u'未选游戏服,请勾选游戏服!')
            return redirect(url_for('ow.owsql'))

        session['indexsql'] = {}
        for db in session.get('serverID'):
            dbsql = OwGame.query.filter_by(serverId=db).first()
            dbhost = dbsql.serverHost
            dbname = dbsql.serverName
            session['dbname'] = dbname
            session['sqlres'] = runSql(dbhost=dbhost,serverid=db,sql=session.get('cmdsql'))
            session.get('indexsql')[db] = session.get('sqlres')

        flash(u'查询数据库完成')
        session['sqldic'] = collections.OrderedDict(sorted(session.get('indexsql').items(),key=lambda t:t[0]))
        # print session.get('sqldic')
        # for k,v in session.get('sqldic').items():
        #     if v:
        #         for sql in v:
        #             for i in sql:
        #                 print '%s : %s' %(i,sql[i])
        return redirect(url_for('ow.owsql'))
    return render_template('ow/owsql.html',
                           commandform=commandform,
                           cmdsql = session.get('cmdsql'),
                           serverlists=serverlists,
                           dbname = session.get('dbname'),
                           sqldic = session.get('sqldic')
                           )

@ow.route('/owRedis',methods=['GET','POST'])
def owRedis():
    return render_template('ow/owRedis.html')

@ow.route('/addOw',methods=['GET','POST'])
def addOw():
    owserverform = OwGameForm()
    if owserverform.validate_on_submit():
        gameserver = OwGame.query.filter_by(serverId=owserverform.id.data).first()
        if gameserver is None:
            gameserver = OwGame(serverId=owserverform.id.data,
                                serverName=owserverform.name.data,
                                serverHost=owserverform.host.data,
                                serverPort=owserverform.port.data)
            db.session.add(gameserver)
            db.session.commit()
            newAnsible = 'ow%s ansible_ssh_host=%s server_port=%s server_id=%s' \
                         %(owserverform.id.data,owserverform.host.data,owserverform.port.data,owserverform.id.data)

            print newAnsible
            os.system("sed -i '/\[ow\]/a\%s' %s" %(newAnsible,ansible_host_file))

            # time.sleep(2)

            #异步添加新服
            app = current_app._get_current_object()
            ThreadAddServer(app,owserverform.id.data,owserverform.port.data)


            flash('add server complete')
            return redirect(url_for('ow.addOw'))
        else:
            flash('serverId is exits')
            return redirect(url_for('ow.addOw'))
    else:
        print 'run out'
    return render_template('ow/addOw.html',owserverform=owserverform)



@ow.route('/updateOw',methods=['GET','POST'])
def updateOw():
    versionform = VersionForm()
    if versionform.validate_on_submit():
        session['proId'] = request.form.get('selectid')
        session['versionNum'] = versionform.version.data
        proId = session.get('proId')
        versionNum = session.get('versionNum')
        app = current_app._get_current_object()
        startRsync(app,proDic,proId,versionNum)
        return redirect(url_for('ow.updateOw'))
    return render_template('ow/updateOw.html',
                           prodict = pronameDict(),
                           versionform = versionform)



def allow_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1] in app.config['ALLOWED_EXTENSIONS']

@ow.route('/upload',methods=['POST','GET'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file and allow_file(file.filename):
            upload_file = path.join(upload_path,secure_filename(file.filename))
            file.save(upload_file)
            session['file_filename'] = file.filename
            print file.filename
            print 'eeee%s' %session.get('file_filename')
            flash('upload file %s complete!' %file.filename)
            return redirect(url_for('ow.PatchOw'))
        else:
            flash('nothin file select or file type error!')
            return redirect(url_for('ow.PatchOw'))
    return render_template('ow/patchOw.html')


@ow.route('/PatchOw',methods=['GET','POST'])
def PatchOw():
    cmdpatch = None
    serverlists = OwGame.query.all()
    patchform = PatchCommandForm()
    if patchform.validate_on_submit():

        stattime = time.strftime("%Y%m%d%H%M%S", time.localtime())
        os.system('cp -rf %s %s_%s' %(patch_logfile,patch_logfile,stattime))
        os.system('echo "" > %s' %patch_logfile)
        os.system('echo "游戏服打补丁开始时间：%s" >> %s' %(stattime,patch_logfile))

        session['cmdpatch'] = patchform.patchcommand.data
        session['serverID'] = request.form.getlist('dbcheckbox')


        #判断是否选服
        if session.get('serverID') == []:
            flash(u'未选游戏服,请勾选游戏服!')
            return redirect(url_for('ow.PatchOw'))

        #判断命令是否包含危险命令
        if any(t in session.get('cmdpatch') for t in warning_command):
            flash(u'命令中包含危险命令,已退出执行')
            return redirect(url_for('ow.PatchOw'))

        if all(t not in session.get('cmdpatch') for t in allow_command):
            flash(u'命令中未包括打补丁的命令,已退出执行')
            return redirect(url_for('ow.PatchOw'))

        for db in session.get('serverID'):
            dbsql = OwGame.query.filter_by(serverId=db).first()
            dbid = dbsql.serverId
            dbhost = dbsql.serverHost
            dbname = dbsql.serverName
            dbport = dbsql.serverPort

            upload_file = path.join(upload_path,secure_filename(session.get('file_filename')))
            app = current_app._get_current_object()
            patchfile = session.get('file_filename')
            patchdir = upload_file
            patchcmd = session.get('cmdpatch')
            serverport = dbport
            serverid = dbid

            #异步执行打补丁操作
            startPatch(app,serverid,patchfile,patchdir,patchcmd,serverport)

        return redirect(url_for('ow.PatchOw'))
    return render_template('ow/patchOw.html',
                           serverlists=serverlists,
                           patchform=patchform,
                           patchfile = session.get('file_filename')
                           )



