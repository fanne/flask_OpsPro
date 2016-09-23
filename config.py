# /usr/bin/python
#coding:utf-8

__Date__ = "2016-03-26 13:53"
__Author__ = 'eyu Fanne'

import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'this is secret key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,'database.sqlite')
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS =True
    UPLOAD_FOLDER = os.path.join(basedir,'app/static/uploads')
    ALLOWED_EXTENSIONS = set(['class'])

    LOGDIR = 'app/static/logs/'
    PATCH_LOGFILE = LOGDIR + 'owpatch_log.text'
    PATCH_OWGLOBAL_LOGFILE = LOGDIR + 'owGlobal_patch_log.text'
    PATCH_OWCROSS_LOGFILE = LOGDIR + 'owCross_patch_log.text'


    @staticmethod
    def init_app(app):
        pass

config = {
    'default':Config

}




