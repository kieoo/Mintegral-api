# !/usr/bin/python
# coding=utf-8

"""
Created on 2017年10月31日

@author: qyke

@step create data befor Scenario

"""

from behave import *
from features.model import publisher
from features.model import app
from features.util import md5_util
from features.plus.handle_data import HandleDate
import hashlib

use_step_matcher('re')

@given(u'创建publisher')
def create_publisher(context, data):

    pub = publisher.Publisher(
        admin_user_id=300,
        username=data['name'],
        email=data['email'],
        passwd=md5_util.md5(data['password']),
        status=1,
        apikey=data['apikey'],
        mv_source_status=1,
        system=3,
        api_status=1,
        permission='1,2,3,4,5'
    )
    try:
        context.user_model = context.sql_session.insert_ex(pub, publisher.Publisher)  # 插入操作,并返回sql插入的结果数据
    except Exception as e:
        print(e)
    return


@given(u'删除publisher')
def del_publisher(context):
    context.sql_session.delete(publisher.Publisher, context.user_model.get('id', 0))
    return


@given(u'创建APP.*保存到(?P<app_tmp>\w+)')
def create_app_and_save(context, app_tmp):
    h_date = HandleDate(context)
    data = h_date.text_eval().get('data')  # 获取data数据
    save_name = h_date.text_eval().get('return')  # 获取保存参数
    my_app = app.App()
    my_app.setApp(data)  # 设置publisher_channel表数据
    context.app_model = {save_name: context.sql_session.insert(my_app)}

