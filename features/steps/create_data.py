# !/usr/bin/python
# coding=utf-8

"""
Created on 2017年10月31日

@author: qyke

@step 前置条件create data befor Scenario

"""

from behave import use_step_matcher, given
from features.model import publisher, app
from features.util import md5_util
from features.lib.handleData import HandleData
from features.config import *
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
        if DEBUG:
            context.user_model = context.sql_session.selectOne(publisher.Publisher, {'id': 12188})
        else:
            # 插入操作,并返回sql插入的结果数据
            context.user_model = context.sql_session.insert_ex(pub, publisher.Publisher)
    except Exception as e:
        print('create user error')
        raise e
    return


@given(u'删除publisher')
def del_publisher(context):
    context.sql_session.delete(publisher.Publisher, context.user_model.get('id', 0))
    return


@given(u'创建.*app.*保存到(?P<app_tmp>\w+)')
def create_app_and_save(context, app_tmp):
    h_data = HandleData(context)
    data = h_data.text_eval().get('data') or h_data.text_eval().get('Data')  # 获取data数据
    save_name = h_data.text_eval().get('save') or h_data.text_eval().get('Save') # 获取保存参数
    my_app = app.App()
    my_app.setApp(data)  # 设置publisher_channel表数据
    context.save_model[save_name] = context.sql_session.insert_ex(my_app, app.App)


@given(u'删除app')
def del_publisher(context):
    h_data = HandleData(context)
    data = h_data.text_eval().get('data') or h_data.text_eval().get('Data') # 获取data数据
    context.sql_session.delete(app.App, data)
    return

