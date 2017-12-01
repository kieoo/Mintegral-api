# !/usr/bin/python
# coding=utf-8

"""
Created on 2017年10月31日

@author: qyke

@step 前置条件create data befor Scenario

"""

from behave import use_step_matcher, given
from features.model import publisher, app
from features.model import *
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


@given(u'准备MYSQL数据.*保存到(?P<app_tmp>\w+)')
def create_app_and_save(context, app_tmp):
    h_data = HandleData(context)
    data_dict = h_data.text_eval()
    model_name = data_dict.get('Model')
    data_dict.pop('Model')
    model = 0
    model_class_list = Base.__subclasses__()    # model父类的所有子类， 注意 需要调用的子类都要 import

    for model_class in model_class_list:  # 遍历Base model子集，声明数据表model对象，并插入数据
        if model_name == getattr(model_class, '__name__'):  # 如果类名与 需要调用的一致，执行操作
            for key, values in data_dict.iteritems():
                model = model_class()
                getattr(model, 'set'+model_name)(values)
                context.save_model[key] = context.sql_session.insert_ex(model, model_class)
    if not model:
        raise Exception('Model name Error')


@given(u'[准备数据|数据准备].*删除.*')
def del_publisher(context):
    h_data = HandleData(context)
    data = h_data.text_eval().get('data') or h_data.text_eval().get('Data') # 获取data数据
    context.sql_session.delete(app.App, data)
    return


@given(u'准备数据.*创建.*')
def create_data_and_save(context):
    h_data = HandleData(context)
    data = h_data.text_eval().get('data') or h_data.text_eval().get('Data')  # 获取data数据
    context.save_model['Tmp_Data'] = data

