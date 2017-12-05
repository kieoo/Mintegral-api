#!/usr/bin/python
# -*- coding: utf-8 -*-
#coding=utf-8
'''
Created on 2015年11月10日

@deprecated: APP持久化类
@author: Linked
'''
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer
from sqlalchemy.sql.sqltypes import String

from features.config import mongo_config
from features.dao.mongo_template import MongoTemplate
from features.dao.sql_template import SqlTemplate
from features.model import Base



class App(Base):

    __tablename__ = 'publisher_channel'
    
    
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer)
    channel_name = Column(String)
    platform = Column(Integer, default=1)
    direct_market = Column(Integer, default=2)
    url = Column(String, default='')
    confirmed_url = Column(String, default='')
    icon = Column(String, default='')
    primary_category = Column(Integer, default=0)
    secondary_category = Column(Integer, default=0)
    grade = Column(Integer, default=0)
    description = Column(String, default='')
    custom = Column(String, default='')
    timestamp = Column(Integer, default=1)
    date = Column(Integer, default=1)
    api = Column(Integer, default=1)
    status = Column(Integer, default=1)
    cfb = Column(Integer, default=1)
    hide_version = Column(String, default='')
    shuffle_version = Column(String, default='')
    landpage_version = Column(String, default='')
    hide_load = Column(Integer, default=2)
    devinfo_encrypt = Column(Integer, default=1)
    proportion = Column(Integer, default=1)
    plct = Column(Integer, default=900)
    plctb = Column(Integer, default=7200)
    postback = Column(String, default='')
    exclude_package = Column(String, default='')
    exclude_advertiser = Column(String, default='')
    campaign_fields = Column(String, default='')
    mtime = Column(Integer, default=0)
    configs = Column(String, default='')
    vba_close = Column(Integer, default=2)
    vba_option = Column(String, default='')
    admin_user_id = Column(Integer, default=1)
    is_incent = Column(Integer, default=2)
    bt_class = Column(Integer, default=0)
    jump_type = Column(Integer, default=1)
    open_type  = Column(Integer, default=1)
    apk_chance = Column(String, default='{"ALL": 100}')
    category = Column(String, default='')
    sub_category = Column(String, default='')
    iab_category = Column(String, default='')
    iab_sub_category = Column(String, default='')
    postback_url = Column(String, default='')
    vta_related_app_id = Column(Integer, default=0)
    vta_related_unit_id = Column(Integer, default=0)
    coppa = Column(Integer, default=2)
    rush_setting = Column(String, default='')
    rush_units = Column(String, default='')
    sub_category_v2 = Column(String, default='')
    iab_category_v2 = Column(String, default='')
    is_sync_category = Column(Integer, default=1)

    def __repr__(self):
        return "<APP(user_id='%d', channel_name='%s', status='%d')>"\
                   % (self.user_id, self.channel_name, self.status)

    
    def setApp(self, appDict):
        for (k, v) in appDict.iteritems():
            setattr(self, k, v)

    
##########################################################
# session = SqlTemplate()
# for obj in session.selectList(App, {'id': 1000000020}):
#     print(object_to_dict(obj))
#    
# mongo = MongoTemplate(host = mongo_config['host'],\
#                                   port = mongo_config['port'],\
#                                   db = mongo_config['db'])
# print(mongo.delete(u'app', {u'appId': 1000000017L}))
    
    