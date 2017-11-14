#!/usr/bin/python
# -*- coding: utf-8 -*-
#coding=utf-8
"""
@deprecated: 全局脚本
@author: Linked
@since: 2015-09-01
@author: Linked
"""

from features.config import mongo_config
from features.dao.mongo_template import MongoTemplate
from features.dao.sql_template import SqlTemplate
from features.dao.request_template import RequestTemplate
from features.config import login_account, mysql_config
from features.steps import create_data
import random
import string


def before_all(context):

    context.sql_session = SqlTemplate(h=mysql_config['host'],
                                        p=mysql_config['port'],
                                        u=mysql_config['username'],
                                        pw=mysql_config['password'])

    random_list = random.sample(string.ascii_letters + string.digits, 32)  # 产生一个32长随机字符数组

    publisher_data = dict()
    publisher_data['name'] = ''.join(random_list)
    publisher_data['email'] = publisher_data['name'] + login_account['email_temp']
    publisher_data['password'] = login_account['password']
    publisher_data['apikey'] = publisher_data['name']

    create_data.create_publisher(context, publisher_data)  # 创建publisher

    context.opener = RequestTemplate(host=login_account['host'],
                                     path=login_account['path'],
                                     email=publisher_data['email'],
                                     password=publisher_data['password'])


def after_all(context):
    pass



def before_scenario(context, scenario):
    pass



def after_scenario(context, scenario):
    pass




