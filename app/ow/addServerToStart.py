# /usr/bin/python
#coding:utf-8

__Date__ = "2016-12-21 10:09"
__Author__ = 'eyu Fanne'

from threading import Thread
from app import create_app
from app.common.myLogConfig import logConfig
import time,os
from subprocess import PIPE,Popen,STDOUT
# from sh import tail


app = create_app('default')
patch_logfile = app.config['ADDSERVER_LOGFILE']


def addStartServer(app,serverid,serverport):
    with app.app_context():
        myfile = open(patch_logfile,"a",0)

        #在服务器上添加新服
        myfile.write("服务器上添加新服执行日志:\n\n")
        myfile.write("添加新服ow%s操作:/data/owserver/ow_op/tools/addserver.sh ow %s %s.\n\n" %(serverid,serverid,serverport))

        p = Popen('source /root/.keychain/CentOS6x64-Int-sh;'
                  '/bin/proxychains /usr/local/python27/bin/ansible ow%s -m shell -a "/data/owserver/ow_op/tools/addserver.sh ow %s %s"'
                  %(serverid,serverid,serverport),
                  stdout=PIPE,stderr=STDOUT,shell=True)
        for line in iter(p.stdout.readline,""):
            myfile.write(line)
            myfile.flush()

        ##在服务器上启动新服
        myfile.write("服务器上启动新服执行日志:\n\n")
        myfile.write("启动新服ow%s操作:/data/owinit/owServer %s start.\n\n" %(serverid,serverport))
        p = Popen('source /root/.keychain/CentOS6x64-Int-sh;'
                  '/bin/proxychains /usr/local/python27/bin/ansible ow%s -m shell -a "/data/owinit/owServer %s start"'
                  %(serverid,serverport),
                  stdout=PIPE,stderr=STDOUT,shell=True)
        for line in iter(p.stdout.readline,""):
            myfile.write(line)
            myfile.flush()

        myfile.write("添加并启动ow%s服完成.\n\n" %serverid)
        myfile.close()


def ThreadAddServer(app,serverid,serverport):
    thr = Thread(target=addStartServer,args=[app,serverid,serverport])
    thr.start()
    return thr