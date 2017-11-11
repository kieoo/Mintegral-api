#!/usr/bin/python
# -*- coding: utf-8 -*-
#coding=utf-8
'''
Created on 2015年11月10日

@deprecated: 广告主持久化类
@author: Linked
'''
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String

from features.config import mongo_config
from features.dao.mongo_template import MongoTemplate
from features.dao.sql_template import SqlTemplate
from features.model import Base
from features.util.common_util import object_to_dict


class Advertiser(Base):

    __tablename__ = 'advertiser_list'
    
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer)
    name = Column(String)
    uniq_key = Column(String)
    title = Column(String)
    desc = Column(String)
    timestamp = Column(Integer)
    status = Column(Integer)
    email = Column(String)
    passwd = Column(String)
    pass_salt = Column(String)
    skype = Column(String)
    tag = Column(Integer)
    balance = Column(Integer)
    
    def __repr__(self):
        return "<Advertiser(id='%d', user_id='%d', name='%s', status='%d')>"\
                   % (self.id, self.user_id, self.name, self.status)
    
    
    def setAdvertiser(self, advDict):
        for (k, v) in advDict.iteritems():
            setattr(self, k, v)
    

#####################################################
# session = SqlTemplate()
# for obj in session.selectList(Advertiser, {'user_id': 7996}):
#     print(object_to_dict(obj))
 
# mongo = MongoTemplate(host = mongo_config['host'],\
#                                   port = mongo_config['port'],\
#                                   db = mongo_config['db'])
# print(mongo.findOne('advertiser', {'advertiserId': 659}))
    
    