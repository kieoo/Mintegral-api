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
    admin_user_id = Column(Integer)
    username = Column(String)
    email = Column(String)
    country = Column(String)
    passwd = Column(String)
    cellphone = Column(String)
    skype = Column(String)
    pass_salt = Column(String)
    status = Column(Integer, default=0)
    timestamp = Column(Integer)
    date = Column(Integer)
    lastlogin = Column(Integer)
    lastname = Column(String)
    firstname = Column(String)
    logo = Column(String)
    company = Column(String)
    address = Column(String)
    apikey = Column(String)
    _from = Column('from', Integer)
    mv_source_status = Column(Integer, default=1)
    resetcode = Column(String)
    system = Column(Integer, default=1)
    know = Column(String)
    api_status = Column(Integer, default=2)
    api_diversity = Column(Integer, default=0)
    offer_priority = Column(Integer, default=0)
    offsetList = Column(String, default='{}')
    forceDeviceId = Column(Integer, default=1)
    register_type = Column(Integer, default=1)
    city_id = Column(Integer, default=0)
    permission = Column(String)

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
