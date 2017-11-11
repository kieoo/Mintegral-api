# !/usr/bin/python
# coding=utf-8

"""
Created on 2017年10月31日

@author: qyke
"""

from behave import *
from hamcrest import *

use_step_matcher('re')

@given(u'请求设置')
def req_setting(context):
    pass

@when(u'请求头')
def req_header(context):
    pass

