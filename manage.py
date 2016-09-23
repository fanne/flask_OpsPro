# /usr/bin/python
#coding:utf-8

__Date__ = "2016-03-25 18:01"
__Author__ = 'eyu Fanne'

from flask_script import Manager,Shell
from flask_migrate import Migrate,MigrateCommand
import logging

from app import create_app,db
from app.models import User,Role,BopGame,OwGame,OwGlobal,OwCross


app = create_app('default')

manager = Manager(app)
migrate = Migrate(app,db)

def make_shell_context():
    return dict(app=app,db=db,User=User,Role=Role,BopGame=BopGame,OwGame=OwGame,OwGlobal=OwGlobal,OwCross=OwCross)

manager.add_command("shell",Shell(make_context=make_shell_context))
manager.add_command("db",MigrateCommand)



if __name__=='__main__':
    manager.run()
    # app.run(debug=True,port=5003,host='0.0.0.0')
