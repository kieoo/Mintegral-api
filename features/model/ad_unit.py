#!/usr/bin/python
# -*- coding: utf-8 -*-
#coding=utf-8
'''
Created on 2015年11月10日

@author: Linked
'''
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer
from sqlalchemy.sql.sqltypes import String

from features.config import mongo_config
from features.config.ad_unit_config import ad_unit01
from features.dao.mongo_template import MongoTemplate
from features.dao.sql_template import SqlTemplate
from features.model import Base
from features.util.common_util import object_to_dict


class AdUnit(Base):

    __tablename__ = 'ad_unit'
    
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer)
    channel_id = Column(Integer)
    ad_unit_name = Column(String)
    pre_click = Column(Integer)
    adtype = Column(Integer)
    orientation = Column(Integer)
    refresh = Column(Integer)
    templates = Column(String)
    sub = Column(Integer)
    image = Column(String)
    switch = Column(Integer)
    frame_num = Column(Integer)
    facebook_placement_id = Column(String)
    ad_source_config = Column(String)
    status = Column(Integer)
    auto_optimize = Column(Integer)
    third_party_request_num = Column(Integer)
    api_request_num = Column(Integer)
    api_cache_num = Column(Integer)
    recall_type = Column(String)
    ctime = Column(Integer)
    mtime = Column(Integer)
    
    def __repr__(self):
        return "<AdUnit(id='%d', user_id='%d', channel_id='%s', ad_unit_name='%s', status='%d')>"\
                   % (self.id, self.user_id, self.channel_id, self.ad_unit_name, self.status)


    def setUnit(self, unitDict):
        for (k, v) in unitDict.iteritems():
            setattr(self, k, v)
        
    
##########################################################
session = SqlTemplate()
for obj in session.selectList(AdUnit, {'id': 600}):
    print(object_to_dict(obj))
    
mongo = MongoTemplate(host = mongo_config['host'],\
                                  port = mongo_config['port'],\
                                  db = mongo_config['db'])
print(mongo.findOne(u'unit', {u'unitId': 600}))

