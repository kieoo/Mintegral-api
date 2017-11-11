#!/usr/bin/python
# -*- coding: utf-8 -*-
#coding=utf-8
"""
Create On 2015年11月11日
@deprecated: 构造mysql数据库引擎，以及Session；
@author: Linked
"""

from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import sessionmaker

from features.config import mysql_config


mysql_engine = create_engine('mysql://%s:%s@%s/%s'\
                                % (mysql_config['username'], mysql_config['password'],\
                                    mysql_config['host'], mysql_config['db'])) #创建Mysql连接
Session = sessionmaker(bind=mysql_engine)


