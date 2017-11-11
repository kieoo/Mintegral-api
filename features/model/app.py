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
from features.util.common_util import object_to_dict



class App(Base):

    __tablename__ = 'publisher_channel'
    
    
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer)
    channel_name = Column(String)
    platform = Column(Integer)
    direct_market = Column(Integer)
    url = Column(String)
    icon = Column(String)
    primary_category = Column(Integer)
    secondary_category = Column(Integer)
    grade = Column(Integer)
    description = Column(Integer)
    custom = Column(String)
    timestamp = Column(Integer)
    date = Column(Integer)
    api = Column(Integer)
    status = Column(Integer)
    devinfo_encrypt = Column(Integer)
    proportion = Column(Integer)
    plct = Column(Integer)
    plctb = Column(Integer)
    postback = Column(String)
    exclude_package = Column(String)
    exclude_advertiser = Column(String)
    campaign_fields = Column(String)
    mtime = Column(Integer)
    admin_user_id = Column(Integer)
    
    def __repr__(self):
        return "<APP(id='%d', user_id='%d', channel_name='%s', status='%d')>"\
                   % (self.id, self.user_id, self.channel_name, self.status)
    
    
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
    
    