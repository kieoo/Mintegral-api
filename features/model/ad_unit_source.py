#!/usr/bin/python
# -*- coding: utf-8 -*-
#coding=utf-8
'''
Created on Mar 1, 2016

@author: linked
'''

from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import String, TIMESTAMP, Integer

from features.model import Base


class AdUnitSource(Base):
    
    __tablename__ = 'ad_unit_source'


    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    ad_unit_id = Column(Integer)
    system = Column(Integer)
    api_app_id = Column(String)
    api_app_key = Column(String)
    ctime = Column(TIMESTAMP)
    mtime = Column(TIMESTAMP)
    
    def __repr__(self):
        return '<AdUnitSource id=%d, user_id=%d, ad_unit_id=%d, system=%d>' \
            % (self.id, self.user_id, self.ad_unit_id, self.system)
    
    
    