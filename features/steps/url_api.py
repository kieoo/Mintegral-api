# !/usr/bin/python
# coding=utf-8

"""
Created on 2017年10月31日

@author: qyke

输入条件
"""

from behave import use_step_matcher, when
from hamcrest import *
from features.lib.handleData import HandleData

use_step_matcher('re')


@when(u'输入参数')
def req_input(context):
    pass


@when(u'输入参数.*?验证返回.*')
def req_input_ex(context):
    data = HandleData(context).text_eval()  # 替换用例函数为运算结果
    path = data.get('Request_url') or data.get('request_url')  # 适配大小写
    method = data.get('Method') or data.get('method')
    param = data.get('Input') or data.get('input')  # 请求体 或者是 请求参数
    output = data.get('Output') or data.get('output')  # 预期输出结果
    if method.lower() == 'post':
        rep = context.opener.post(path, param)
    else:
        rep = context.opener.get(path, param)

    assert_that(rep, is_not(0), 'TEST CASE: <' + context.scenario.name + '> : 失败！')

    rep_dict = eval(rep)
    assert_that(output, has_entries(rep_dict), 'TEST CASE: <' + context.scenario.name + '> : 失败！')
