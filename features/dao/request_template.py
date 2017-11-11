#!/usr/bin/python
# coding=utf-8
'''
Created on 2017年11月02日

@author: qyke
'''

import urllib2
import urllib
import cookielib
import re


class RequestTemplate:

    def __init__(self, host, path, email, password, protocol='http'):
        self.header = []
        self.session = {}
        self.host = host

        self.cj = cookielib.CookieJar()  # 创建一个cookie管理器
        handler = urllib2.HTTPCookieProcessor(self.cj)

        self.opener = urllib2.build_opener(handler)  # 创建一个opener

        self.login(protocol, path, email, password)  # 执行登录操作，以获得token, publisher_id

        self.opener.addheaders = self.header

    def login(self, l_pro, l_path, l_email, l_pw):
        login_url = '{0}://{1}{2}'.format(l_pro, self.host, l_path['login_url'])
        user = l_email
        password = l_pw
        post_data = urllib.urlencode({'email': user, 'password': password})
        self.header.extend([('Referer', login_url)])
        self.opener.addheaders = self.header
        try:
            response = self.opener.open(login_url, post_data)
            code = re.search(r'code=(\S+)', response.url).group(1)  # 获取登录code
        except Exception as e:
            print('login error!')
            raise e
        else:
            if code:
                access_url = '{0}://{1}{2}'.format(l_pro, self.host, l_path['token_url'])
                self.header.extend([('Accept', 'application/json, text/plain, */*')])
                self.opener.addheaders = self.header
                post_data = urllib.urlencode({'code': code})
                try:
                    response = self.opener.open(access_url, post_data).read()
                    response_data = eval(response).get('data')
                    # 将accession 加到请求头
                    self.add_header(ACCESSTOKEN=response_data.get('access_token'),
                                    PUBLISHERID=response_data.get('publisher_id'))
                    self.session = response_data
                except Exception as e:
                    print('get token error!')
                    raise e

            else:
                raise Exception('get code error!')

    def get_session(self):
        '''
        :return:(dist){'publisher_id':'', 'access_token:':''}
        '''
        return self.session

    def cookie_setting(self, *args, **kwargs):
        pass

    def add_header(self, *args, **kwargs):
        '''
        :param args: (header_name:values),
        :param kwargs: header_name=values,
        :return:
        '''
        if args:
            for tmp in args:
                for k, v in tmp.items():
                    self.header.append((k, v))

        if kwargs:
            for k, v in kwargs.items():
                self.header.append((k, v))
        return

    def head_setting(self, *args, **kwargs):
        pass

    def post(self, *args, **kwargs):
        pass

    def get(self, *args, **kwargs):
        pass
