# /usr/bin/python
#coding:utf-8

__Date__ = "2016-04-07 16:00"
__Author__ = 'eyu Fanne'

import os
import paramiko
import commands
import time

from myLogConfig import logConfig
from threading import Thread


class svnRsyncPro():
    #####
    #：预留logger参数，传入logger参数后开始记录日志
    ####
    def __init__(self,logger):
        self.logger =logger

    def testfun(self,test):
        self.logger.info('ddddddddddd%s' %test)
    def setlog(self):
        pass
        
    def get_version(self,pro):
        self.logger.info('内网版本svn信息:')
        self.logger.info(os.popen('svn info %s' %pro).read().strip())

    def online_laste(self,dir_pro,pro_name):
        self.logger.info('更新本地外网%s的svn到最新版本' %pro_name)
        self.logger.info(os.popen('svn up %s' %dir_pro).read().strip())

    def up_svn(self,pro_version,pro):
        self.logger.info('更新内网svn版本为%s' %pro_version)
        self.logger.info(os.popen('svn up -r %d %s' %(int(pro_version),pro)).read().strip())

    def rsync_file(self,local_dir,online_dir,pro_name):
        self.logger.info('同步内网%s svn到外网svn' %pro_name)
        self.logger.info('%s,%s' %(local_dir,online_dir))
        self.logger.info(os.popen('rsync -avrz --exclude=".svn" --delete   %s %s' %(local_dir,online_dir)).read().strip())

    def add_commit(self,online_dir,pro_name,pro_version):
        self.logger.info("开始提交%s版本到外网服SVN。" %pro_name)
        #删除不存在文件
        svn_status_del = os.popen("svn st %s|grep ^\!" %online_dir).readlines()
        if svn_status_del != []:
            for del_i in svn_status_del:
                del_j = del_i.split()[1]
                self.logger.info(os.popen('svn del %s' %del_j).read().strip())
        #添加所有文件到svn上
        svn_status_add = os.popen("svn st %s|grep ^?" %online_dir).readlines()
        if svn_status_add != []:
            self.logger.info(os.popen('svn add --force %s' %online_dir).read().strip())

        #提交所有内容到svn上
        self.logger.info(os.popen('svn ci -m "提交%s的内网版本号%s" %s' %(pro_name,pro_version,online_dir)).read().strip())
        #最后再次判断svn状态
        svn_status = os.popen("svn st %s" %online_dir).read()
        if svn_status != "":
            self.logger.info("提交到外网svn的版本有误，请手动修改，当外网svn状态:")
            self.logger.info(svn_status)
        self.logger.info("完成提交%s项目的内网SVN版本到外网svn完毕。" %pro_name)

    def ssh_cmd(self,hostname,cmd,pro_name):
        self.logger.info("对外网服务器%s操作svn up指令中...." %hostname)
        self.logger.info('%s %s' %(pro_name,hostname))
        username="root"
        password="qwe34%^QWE"
        pkey_w='keyfile/1254'
        try:
            pkey=paramiko.RSAKey.from_private_key_file(pkey_w)
        except paramiko.PasswordRequiredException:
            pkey=paramiko.RSAKey.from_private_key_file(pkey_w,password)
        ssh=paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname,port=23111,username=username,pkey=pkey)
        for cmd_a in cmd:
            stdin,stdout,stderr=ssh.exec_command(cmd_a)
            out=stdout.readlines()
            errout=stderr.readlines()
            for o in out:
                self.logger.info(o)
            for err_o in errout:
                self.logger.info(err_o)
        self.logger.info("外网服务器%s操作svn up指令完毕。" %hostname)




