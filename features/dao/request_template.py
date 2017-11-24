#!/usr/bin/python
# coding=utf-8
"""
Created on 2017年11月02日

@author: qyke

接口登录类，封装需要的请求session到请求头
"""

import urllib2
import urllib
import cookielib
from hamcrest import *
from features.lib.access import Access
from features.config import *


class RequestTemplate:

    def __init__(self, host, path, email, password, protocol='http'):
        self.header = []
        self.session = {}
        self.host = host
        self.protocol = protocol
        # 创建一个cookie管理器
        self.cj = cookielib.CookieJar()
        cookie_handler = urllib2.HTTPCookieProcessor(self.cj)
        # 创建重定向管理
        redirect_handler = urllib2.HTTPRedirectHandler()
        # 创建一个opener
        self.opener = urllib2.build_opener(cookie_handler, redirect_handler)
        # 执行登录操作，以获得token, publisher_id
        self.access(protocol, host, path, email, password)

    def access(self, pro, h, pa, em, pd):

        user_access = Access(self.opener, pro, h, pa)
        # 登录获取session 重试三次
        for i in range(2):
            try:
                user_access.login(em, pd)  # 执行登录请求
            except Exception as e:
                if i > 1:
                    raise e
                else:
                    pass
            else:
                break
        # 将access session 加到请求头
        self.session = user_access.get_session()
        self.add_header(ACCESSTOKEN=self.session.get('access_token'),
                        PUBLISHERID=self.session.get('publisher_id'))

    def get_session(self):
        """
        :return:(dist){'publisher_id':'', 'access_token:':''}
        """
        return self.session

    def cookie_setting(self, *args, **kwargs):
        pass

    def add_header(self, *args, **kwargs):
        """
        :param args: {header_name:values, header_name2:values2},{},……
        :param kwargs: header_name=values,header_name2=values2
        :return:
        """
        if args:
            for tmp in args:
                for k, v in tmp.items():
                    self.header.append((k, v))

        if kwargs:
            for k, v in kwargs.items():
                self.header.append((k, v))

        self.opener.addheaders.extend(self.header)

        return

    def head_setting(self, *args, **kwargs):
        pass

    def post(self, path, body, timeout=HTTP_TIMEOUT):
        """
        :param path: str 请求url path
        :param body: dict body 内容
        :param redirects: 是否重定向
        :param timeout: int 超时时间 second
        :return: str
        """
        url = '{0}://{1}/{2}'.format(self.protocol, self.host, path.strip('/'))  # 模糊匹配path首位有 / 没 / 的情况
        body = urllib.urlencode(body)
        for i in range(1):
            try:
                res = self.opener.open(url, body, timeout=timeout)
                return res.read()
            except urllib2.HTTPError as e:
                assert_that(i, less_than(1), 'POST [{0}] ERROR CODE:{1} '.format(path, e.code))
                pass
        return 0

    def get(self, path, param, timeout=HTTP_TIMEOUT):
        """
        :param path: str 请求url path
        :param param: dict get 请求参数
        :param redirects: 是否重定向
        :param timeout: int second
        :return:
        """
        url = '{0}://{1}/{2}'.format(self.protocol, self.host, path.strip('/'))  # 模糊匹配path首位有 / 没 / 的情况
        param_list = []
        for key, value in param:
            param_list.append(key + '=' + value)
        param_str = '&'.join(param_list)
        url += '?' + param_str
        for i in range(1):
            try:
                res = self.opener.open(url, timeout=timeout)
                return res.read()
            except urllib2.HTTPError as e:
                assert_that(i, less_than(1), 'GET [{0}] ERROR CODE:{1} '.format(path, e.code))
                pass
        return 0
