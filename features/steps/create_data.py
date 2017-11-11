# !/usr/bin/python
# coding=utf-8

"""
Created on 2017年10月31日

@author: qyke

@step create data befor Scenario

"""

from behave import *
from features.model import publisher
from features.util import md5_util
import hashlib

use_step_matcher('re')


@given(u'创建APP')
def req_setting(context):
    pass


@given(u'创建publisher')
def create_publisher(context, data):

    pub = publisher.Publisher(
        admin_user_id=300,
        username=data['name'],
        email=data['email'],
        country='CN',
        passwd=md5_util.md5(data['password']),
        cellphone='1',
        skype='',
        pass_salt='',
        status=1,
        timestamp=1,
        date=1,
        lastlogin=1,
        lastname='',
        firstname='',
        logo='',
        company='',
        address='',
        apikey=data['apikey'],
        _from=0,
        mv_source_status=1,
        resetcode='',
        system=3,
        know='',
        api_status=1,
        permission='1,2,3,4,5'
    )

    context.sql_session.insert(pub)
    return


@given(u'删除publisher')
def del_publisher(context):
    pass