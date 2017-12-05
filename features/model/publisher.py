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

from features.model import Base


class Publisher(Base):

    __tablename__ = 'user_info'
    
    id = Column(Integer, primary_key=True)
    relative_user_id = Column(Integer, default=0)
    admin_user_id = Column(Integer, default=1)
    username = Column(String)
    email = Column(String)
    country = Column(String, default='CN')
    passwd = Column(String)
    cellphone = Column(String, default='')
    skype = Column(String, default='')
    pass_salt = Column(String, default='')
    status = Column(Integer, default=0)
    timestamp = Column(Integer, default=1)
    date = Column(Integer, default=1)
    lastlogin = Column(Integer, default=1)
    lastname = Column(String, default='')
    firstname = Column(String, default='')
    logo = Column(String, default='')
    company = Column(String, default='')
    address = Column(String, default='')
    apikey = Column(String, default='')
    _from = Column('from', Integer, default=1)
    mv_source_status = Column(Integer, default=1)
    resetcode = Column(String, default='')
    system = Column(Integer, default=1)
    know = Column(String, default='')
    api_status = Column(Integer, default=1)
    api_diversity = Column(Integer, default=0)
    offer_priority = Column(Integer, default=0)
    offsetList = Column(String, default='{}')
    forceDeviceId = Column(Integer, default=1)
    register_type = Column(Integer, default=1)
    city_id = Column(Integer, default=0)
    permission = Column(String, default='')

    def __repr__(self):
#        return "<Publisher(id='%d', username='%s', status='%d', system=%d, email=%s)>"\
#                    % (self.id, self.username, self.status, self.system, self.email)
        return "<Publisher( username='%s', status='%d', system=%d, email=%s)>"\
                   % (self.username, self.status, self.system, self.email)

    def setPublisher(self, pubDict):
        for (k, v) in pubDict.iteritems():
            setattr(self, k, v)
    

############################################
# session = SqlTemplate()
# print(object_to_dict(session.selectOne(Publisher, {'id': 7996})))
