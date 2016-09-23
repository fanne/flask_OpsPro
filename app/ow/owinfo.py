# /usr/bin/python
#coding:utf-8

__Date__ = "2016-04-07 18:30"
__Author__ = 'eyu Fanne'

import collections

global_dir=r'/data/projectDir/owpro/ow_svn_192/release_owglobal/'
server_dir=r'/data/projectDir/owpro/ow_svn_192/release_s1/'
charge_dir=r'/data/projectDir/owpro/ow_svn_192/release_h5game_charge_server/'
proxy_dir=r'/data/projectDir/owpro/ow_svn_192/release_owadmin/'
push_dir=r'/data/projectDir/owpro/ow_svn_192/release_push/'
trans_dir=r'/data/projectDir/owpro/ow_svn_192/release_trans/'
client_app_dir=r'/data/projectDir/owpro/ow_svn_192/owclient_app/'
client_web_dir=r'/data/projectDir/owpro/ow_svn_192/owclient_web/'
owfbinv_dir=r'/data/projectDir/owpro/ow_svn_192/owfbinv/'
cross_kings_feast_dir=r'/data/projectDir/owpro/ow_svn_192/release_cross_kings_feast/'
owgift_dir=r'/data/projectDir/owpro/ow_svn_192/release_gift_server/'


global_OL_dir=r'/data/projectDir/owpro/ow_svn_online/owglobal/'
server_OL_dir=r'/data/projectDir/owpro/ow_svn_online/owserver/'
charge_OL_dir=r'/data/projectDir/owpro/ow_svn_online/owcharge/'
proxy_OL_dir=r'/data/projectDir/owpro/ow_svn_online/owproxy/'
push_OL_dir=r'/data/projectDir/owpro/ow_svn_online/owpush/'
trans_OL_dir=r'/data/projectDir/owpro/ow_svn_online/owtrans/'
client_OL_app_dir=r'/data/projectDir/owpro/ow_svn_online/owclient_hw/'
client_OL_web_dir=r'/data/projectDir/owpro/ow_svn_online/owweb/'
owfbinv_OL_dir=r'/data/projectDir/owpro/ow_svn_online/owfbinv/'
cross_kings_feast_OL_dir=r'/data/projectDir/owpro/ow_svn_online/owcross/'
owgift_OL_dir=r'/data/projectDir/owpro/ow_svn_online/owgift/'


proDic={
    "1001": {"pro_name":u"全球服","pro_dir":"%s" %global_dir,"ol_dir":"%s" %global_OL_dir},
    "1002": {"pro_name":u"游戏服","pro_dir":"%s" %server_dir,"ol_dir":"%s" %server_OL_dir},
    "1003": {"pro_name":u"充值服","pro_dir":"%s" %charge_dir,"ol_dir":"%s" %charge_OL_dir},
    "1004": {"pro_name":u"中转服(代理服)","pro_dir":"%s" %proxy_dir,"ol_dir":"%s" %proxy_OL_dir},
    "1005": {"pro_name":u"推送服","pro_dir":"%s" %push_dir,"ol_dir":"%s" %push_OL_dir},
    "1006": {"pro_name":u"翻译服","pro_dir":"%s" %trans_dir,"ol_dir":"%s" %trans_OL_dir},
    "1007": {"pro_name":u"web客户端(cdn)","pro_dir":"%s" %client_web_dir,"ol_dir":"%s" %client_OL_web_dir},
    "1008": {"pro_name":u"app客户端(手机端)", "pro_dir":"%s" %client_app_dir,"ol_dir":"%s" %client_OL_app_dir},
    "1009": {"pro_name":u"facebook好友服", "pro_dir":"%s" %owfbinv_dir,"ol_dir":"%s" %owfbinv_OL_dir},
    "1010": {"pro_name":u"跨服", "pro_dir":"%s" %cross_kings_feast_dir,"ol_dir":"%s" %cross_kings_feast_OL_dir},
    "1011": {"pro_name":u"礼包服", "pro_dir":"%s" %owgift_dir,"ol_dir":"%s" %owgift_OL_dir},
}




def pronameDict():
    pro_dic={}
    for key,value in proDic.items():
        pro_dic.setdefault('%s' %key,'%s' %value['pro_name'])
    pro_dic = collections.OrderedDict(sorted(pro_dic.items(),key=lambda t:t[0]))
    return pro_dic