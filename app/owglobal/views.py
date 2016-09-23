# /usr/bin/python
#coding:utf-8

__Date__ = "2016-07-01 16:05"
__Author__ = 'eyu Fanne'

from flask import render_template,url_for,session,request,flash,redirect,current_app
from .import owglobal
from ..models import OwGlobal
from .forms import PatchCommandForm
from os import path
from app import create_app
from werkzeug.utils import secure_filename
from globalpatch import startPatch
import time,os


app = create_app('default')
upload_path = app.config['UPLOAD_FOLDER']
if not os.path.exists(upload_path):
    os.mkdir(upload_path)


warning_command = ['init','stop','start','restart','kill',';','&&','root','tmp','h5game']
allow_command = ['patch','com.my9yu.owglobal.patch']
patch_logfile = app.config['PATCH_OWGLOBAL_LOGFILE']
print patch_logfile


def allow_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1] in app.config['ALLOWED_EXTENSIONS']


@owglobal.route('/globalupload',methods=['POST','GET'])
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
            return redirect(url_for('owglobal.PatchOwGlobal'))
        else:
            flash('nothin file select or file type error!')
            return redirect(url_for('owglobal.PatchOwGlobal'))
    return render_template('owglobal/patchOwGlobal.html')

@owglobal.route('/PatchOwGlobal',methods=['GET','POST'])
def PatchOwGlobal():
    cmdpatch = None
    serverlists = OwGlobal.query.all()
    patchform = PatchCommandForm()
    if patchform.validate_on_submit():

        stattime = time.strftime("%Y%m%d%H%M%S", time.localtime())
        os.system('cp -rf %s %s_%s' %(patch_logfile,patch_logfile,stattime))
        os.system('echo "" > %s' %patch_logfile)
        os.system('echo "全球服打补丁开始时间：%s" >> %s' %(stattime,patch_logfile))

        session['cmdpatch'] = patchform.patchcommand.data
        session['serverID'] = request.form.getlist('dbcheckbox')


        #判断是否选服
        if session.get('serverID') == []:
            flash(u'未选游戏服,请勾选游戏服!')
            return redirect(url_for('owglobal.PatchOwGlobal'))

        #判断命令是否包含危险命令
        if any(t in session.get('cmdpatch') for t in warning_command):
            flash(u'命令中包含危险命令,已退出执行')
            return redirect(url_for('owglobal.PatchOwGlobal'))

        if all(t not in session.get('cmdpatch') for t in allow_command):
            flash(u'命令中未包括打补丁的命令,已退出执行')
            return redirect(url_for('owglobal.PatchOwGlobal'))

        for db in session.get('serverID'):
            dbsql = OwGlobal.query.filter_by(serverId=db).first()
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

        return redirect(url_for('owglobal.PatchOwGlobal'))
    return render_template('owglobal/patchOwGlobal.html',
                           serverlists=serverlists,
                           patchform=patchform,
                           patchfile = session.get('file_filename')
                           )