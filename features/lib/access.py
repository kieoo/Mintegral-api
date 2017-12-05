#!/usr/bin/python
# coding=utf-8
"""

Created on 2017年11月22日

@author: qyke

登录验证权限类

"""

import urllib
import re


class Access(object):

    session = dict()
    header = []

    def __init__(self, opener, pro, host, path):
        self.login_url = '{0}://{1}/{2}'.format(pro, host, path['login_url'].strip('/'))  # 模糊匹配path首位有 / 没 / 的情况
        self.access_url ='{0}://{1}/{2}'.format(pro, host, path['token_url'].strip('/'))
        self.opener = opener

    def login(self, l_email, l_pw):
        """
        登录并保存session到对象变量
        :param l_email: 用户邮箱
        :param l_pw: 用户密码
        :return:
        """
        user = l_email
        password = l_pw
        post_data = urllib.urlencode({'email': user, 'password': password})
        self.header.extend([('Referer', self.login_url)])  # 登录需要验证referer
        self.opener.addheaders = self.header
        try:
            response = self.opener.open(self.login_url, post_data)
            code_match = re.search(r'code=(\S+)', response.url)  # 获取登录code
            code = ''
            if code_match:
                code = code_match.group(1)
        except Exception as e:
            print('login error!')
            raise(e)
        else:
            if code:
                self.header.extend([('Accept', 'application/json, text/plain, */*')])  # 取得code后 获取登录session
                self.opener.addheaders = self.header
                post_data = urllib.urlencode({'code': code})
                try:
                    response = self.opener.open(self.access_url, post_data).read()
                    response_data = eval(response).get('data')
                    if response_data.get('access_token') and response_data.get('publisher_id'):
                        pass
                    else:
                        raise Exception('get token error!')
                    self.session = response_data
                except Exception as e:
                    print('get token error!')
                    raise e

            else:
                raise Exception('get code error!')

    def get_session(self):

        return self.session

