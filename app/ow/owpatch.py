# /usr/bin/python
#coding:utf-8

__Date__ = "2016-06-02 17:39"
__Author__ = 'eyu Fanne'

from threading import Thread
from app import create_app
from app.common.myLogConfig import logConfig
import time,os
from subprocess import PIPE,Popen,STDOUT
# from sh import tail


app = create_app('default')
patch_logfile = app.config['PATCH_LOGFILE']



def PatchWork(app,serverid,patchfile,patchdir,patchcmd,serverport):
    with app.app_context():
        myfile = open(patch_logfile,"a",0)

        # p = Popen('source /root/.keychain/CentOS6x64-Int-sh;'
        #           '/usr/local/python27/bin/ansible ow%s -m ping' %serverid,
        #           stdout=PIPE,stderr=STDOUT,shell=True)
        # for line in iter(p.stdout.readline,""):
        #     myfile.write(line)
        #     myfile.flush()

        #文件拷贝到远程机器
        p = Popen('source /root/.keychain/CentOS6x64-Int-sh;'
                  '/usr/local/python27/bin/ansible ow%s -m copy -a "src=%s dest=/tmp"' %(serverid,patchdir),
                  stdout=PIPE,stderr=STDOUT,shell=True)
        for line in iter(p.stdout.readline,""):
            myfile.write(line)
            myfile.flush()

        ##执行远程机补丁命令
        myfile.write("执行ow_%s服补丁命令操作:/data/owinit/owServer %s patch %s /tmp/%s.\n\n" %(serverid,serverport,patchcmd,patchfile))
        p = Popen('source /root/.keychain/CentOS6x64-Int-sh;'
                  '/usr/local/python27/bin/ansible ow%s -m shell -a "/data/owinit/owServer %s patch %s /tmp/%s"' %(serverid,serverport,patchcmd,patchfile),
                  stdout=PIPE,stderr=STDOUT,shell=True)
        for line in iter(p.stdout.readline,""):
            myfile.write(line)
            myfile.flush()

        ##打印打补丁后的日志信息
        myfile.write("补丁执行日志:\n\n")
        p = Popen('source /root/.keychain/CentOS6x64-Int-sh;'
                  '/usr/local/python27/bin/ansible ow%s -m shell -a "tail -n 5 /data/owserver/%s/logs/logs"' %(serverid,serverport),
                  stdout=PIPE,stderr=STDOUT,shell=True)
        for line in iter(p.stdout.readline,""):
            myfile.write(line)
            myfile.flush()

        myfile.write("执行ow%s服完成.\n\n" %serverid)
        myfile.close()


def startPatch(app,serverid,patchfile,patchdir,patchcmd,serverport):
    thr = Thread(target=PatchWork,args=[app,serverid,patchfile,patchdir,patchcmd,serverport])
    thr.start()
    return thr


