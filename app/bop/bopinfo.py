# /usr/bin/python
#coding:utf-8

__Date__ = "2016-04-08 10:43"
__Author__ = 'eyu Fanne'

import collections

global_dir=r'/data/projectDir/boppro/bop_svn_192/release_bopglobal/'
server_dir=r'/data/projectDir/boppro/bop_svn_192/release_s1/'
charge_dir=r'/data/projectDir/boppro/bop_svn_192/release_charge_server/'
proxy_dir=r'/data/projectDir/boppro/bop_svn_192/release_bopadmin/'
push_dir=r'/data/projectDir/boppro/bop_svn_192/release_push/'
trans_dir=r'/data/projectDir/boppro/bop_svn_192/release_trans/'
client_app_dir=r'/data/projectDir/boppro/bop_svn_192/bopclient_app/'
client_web_dir=r'/data/projectDir/boppro/bop_svn_192/bopclient_web/'


global_OL_dir=r'/data/projectDir/boppro/bop_svn_online/bopglobal/'
server_OL_dir=r'/data/projectDir/boppro/bop_svn_online/bopserver/'
charge_OL_dir=r'/data/projectDir/boppro/bop_svn_online/bopcharge/'
proxy_OL_dir=r'/data/projectDir/boppro/bop_svn_online/bopproxy/'
push_OL_dir=r'/data/projectDir/boppro/bop_svn_online/boppush/'
trans_OL_dir=r'/data/projectDir/boppro/bop_svn_online/boptrans/'
client_OL_app_dir=r'/data/projectDir/boppro/bop_svn_online/bopclient/'
client_OL_web_dir=r'/data/projectDir/boppro/bop_svn_online/bopweb/'



proDic={
    "1001": {"pro_name":u"全球服","pro_dir":"%s" %global_dir,"ol_dir":"%s" %global_OL_dir},
    "1002": {"pro_name":u"游戏服","pro_dir":"%s" %server_dir,"ol_dir":"%s" %server_OL_dir},
    "1003": {"pro_name":u"充值服","pro_dir":"%s" %charge_dir,"ol_dir":"%s" %charge_OL_dir},
    "1004": {"pro_name":u"中转服(代理服)","pro_dir":"%s" %proxy_dir,"ol_dir":"%s" %proxy_OL_dir},
    # "1005": {"pro_name":u"推送服","pro_dir":"%s" %push_dir,"ol_dir":"%s" %push_OL_dir},
    "1006": {"pro_name":u"翻译服","pro_dir":"%s" %trans_dir,"ol_dir":"%s" %trans_OL_dir},
    "1007": {"pro_name":u"web客户端(cdn)","pro_dir":"%s" %client_web_dir,"ol_dir":"%s" %client_OL_web_dir},
    "1008": {"pro_name":u"app客户端(手机端)", "pro_dir":"%s" %client_app_dir,"ol_dir":"%s" %client_OL_app_dir},
}


def pronameDict():
    pro_dic={}
    for key,value in proDic.items():
        pro_dic.setdefault('%s' %key,'%s' %value['pro_name'])
    pro_dic = collections.OrderedDict(sorted(pro_dic.items(),key=lambda t:t[0]))
    return pro_dic