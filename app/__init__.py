# /usr/bin/python
#coding:utf-8

__Date__ = "2016-03-25 17:50"
__Author__ = 'eyu Fanne'

from flask import Flask
from flask_wtf import Form
from flask_nav import Nav
from flask_nav.elements import Navbar,View,Link,Subgroup,Separator
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config


bootstrap = Bootstrap()
nav = Nav()
db = SQLAlchemy()


nav.register_element('top',Navbar(
    View('Home','main.index'),
    Subgroup(
        'SQL Query',
        View('OwSql','ow.owsql',product='owsql'),
        View('BopSql','bop.bopsql',product='bopsql'),
        View('CrossSql','owcross.crosssql',product='crosssql'),
    ),
    Subgroup(
        'Redis Query',
        View('OwRedis','ow.owRedis',product='owRedis'),
        View('BopRedis','bop.bopRedis',product='bopRedis')
    ),
    Subgroup(
        'Add Server',
        View('addOw', 'ow.addOw', product='addOw'),
        View('addBop', 'bop.addBop', product='addBop'),
        Separator(),
        View('Wg10X', 'main.products', product='wg10x'),
        ),
    View('ServerList','main.getdata'),
    View('initServer','main.initserver'),
    Subgroup(
        'Update Server',
        View('updateOw','ow.updateOw',product='updateOw'),
        View('updateBop','bop.updateBop',product='updateBop')
        ),
    Subgroup(
        'Patch',
        View('游戏服','ow.PatchOw',product='PatchOw'),
        View('全球服','owglobal.PatchOwGlobal',product='PatchOwGlobal'),
        View('跨服','owcross.PatchOwCross',product='PatchOwCross'),
        ),
    ))


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    nav.init_app(app)
    db.init_app(app)
    from .main import main as main_blueprint
    from .bop import bop as bop_blueprint
    from .ow import ow as ow_blueprint
    from .owglobal import owglobal as owglobal_blueprint
    from .owcross import owcross as owcross_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(bop_blueprint)
    app.register_blueprint(ow_blueprint)
    app.register_blueprint(owglobal_blueprint)
    app.register_blueprint(owcross_blueprint)
    return app
