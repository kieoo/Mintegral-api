#!/usr/bin/python
# coding=utf-8

"""
Create On 2017年11月1日

@deprecated: 全局配置表
"""

# -------------------- 测试脚本配置 ---------------------
DEBUG = 1
SCENARIO_RETRY = 1  # 用例失败重试次数
HTTP_TIMEOUT = 5  # 接口超时时间 second

# -------------------- 权限配置 -------------------------

login_account = {
                 'host': 'qyke-dev.mintegral.net',
                 'email_temp': '@mobvista.com',
                 'password': '1',
                 'path': {
                     'login_url': '/user/verify',
                     'token_url': '/login/access_token'  # 路径头 加 '/' 不加 '/' 都可
                    },
                }

# -------------------- 数据库配置 -------------------------
                                                                                                                                                                                                             
mysql_config = {
                'username': 'root',
                'password': 'TNKq6de8ttjGq4aB',
                'host': '13.228.53.100',
                'port': 3306,
                'db': 'mob_adn'
                }

mongo_config = {
                # 'host':'127.0.0.1',
                'host': '52.74.240.202',
                'port': 27017,
                'db': 'new_adn'
                }

mongo_collection_names = {
                          'sdk_plugin': 'sdkPlugins', 
                          'publisher_channel': 'app',
                          'ad_unit': 'unit',
                          'advertiser_list': 'advertiser',
                          'campaign_list': 'campaign' 
                          }




