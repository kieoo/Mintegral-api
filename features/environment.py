#!/usr/bin/python
# coding=utf-8

"""
@deprecated: 全局脚本
@author: qyke
@since: 2017-11-01

"""
from features.dao.sql_template import SqlTemplate
from features.dao.request_template import RequestTemplate
from features.config import *
from features.steps import create_data
import random
import string
from behave.contrib.scenario_autoretry import patch_scenario_with_autoretry


def before_all(context):
    # 持久化数据库
    context.sql_session = SqlTemplate(h=mysql_config['host'],
                                        p=mysql_config['port'],
                                        u=mysql_config['username'],
                                        pw=mysql_config['password'])

    random_list = random.sample(string.ascii_letters + string.digits, 32)  # 产生一个32长随机字符数组

    # 持久化http接口（访问权限）
    publisher_data = dict()
    publisher_data['name'] = ''.join(random_list)
    publisher_data['email'] = publisher_data['name'] + login_account['email_temp']
    publisher_data['password'] = login_account['password']
    publisher_data['apikey'] = publisher_data['name']

    # 创建publisher
    create_data.create_publisher(context, publisher_data)

    if DEBUG:

        context.opener = RequestTemplate(host=login_account['host'],
                                         path=login_account['path'],
                                         email='a3t8TC1wJylpgrUBiZLP2zoj6neSGb0A@mobvista.com',
                                         password='1')
    else:

        context.opener = RequestTemplate(host=login_account['host'],
                                         path=login_account['path'],
                                         email=publisher_data['email'],
                                         password=publisher_data['password'])
    # 声明一个公有dict，供用例存储数据
    context.save_model = dict()


def after_all(context):  # TODO
    pass


def before_feature(context, feature):
    for scenario in feature.scenarios:
        if 'autoretry' in scenario.effective_tags:
            patch_scenario_with_autoretry(scenario, max_attempts=SCENARIO_RETRY)


def before_scenario(context, scenario):  # TODO
    pass


def after_scenario(context, scenario):  # TODO
    pass




