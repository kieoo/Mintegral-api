#!/usr/bin/python
# coding=utf-8

'''

Created on 2017年11月14日

@author: qyke

处理features用例数据 类

'''


import re
from features.util import func_util

func_re = re.compile(r'\$__fun\((?P<func_name>\w+),(?P<func_param>.*?)\)', re.I)
param_re = re.compile(r'\$\{(?P<save_name>[A-Za-z0-9]+)\.(?P<save_key>[A-Za-z0-9]+)\}')

class HandleData(object):

    def __init__(self, context):
        self.datas_original_str = context.text
        self.datas_rel = ''
        self.handle_context = context
        self.check_ini_data()  # TODO
        self.transfuc()
        self.tansparam()

    def text_eval(self):
        try:
            datas_dict = eval(self.datas_rel)
        except Exception as e:
            print('Incorrect Dict Format=> ' + self.datas_rel)
            raise e
        return datas_dict

    def transfuc(self):
        """
            匹配context data中$__func()，拼装回text
        """
        for data in self.datas_original_str.split('\n'):
            ma = func_re.finditer(data)     # 匹配每行$__func()
            for func in ma:                 # 匹配行内每个$__func()
                func_list = func.groupdict()
                func_value = self.func_exec(func_list['func_name'], func_list['func_param'])
                data = func_re.sub(str(func_value), data, 1)    # 每次替换一个$__func() 为
            self.datas_rel += data + '\n'   # 拼装回text

        return

    def transparam(self):
        """
        匹配context data 中 ${}, 拼装回text
        :return:
        """
        for data in self.datas_original_str.split('\n'):
            ma = param_re.finditer(data)     # 匹配每行$__func()
            for param in ma:                 # 匹配行内每个$__func()
                param_list = param.groupdict()
                param_value = self.func_exec('get_save_info',
                                             param_list['save_name']+','+param_list['save_key'])  # TODO
                data = param_re.sub(str(param_value), data, 1)    # 每次替换一个$__func() 为
            self.datas_rel += data + '\n'   # 拼装回text

        return

    def func_exec(self, name, param):
        """
        执行context data中$__func()，返回values
        :param name: string, function name
        :param param: list, param
        :return: string
        """
        func_name = getattr(func_util, name)
        func_param_tp = eval(param)
        if not isinstance(func_param_tp, tuple):
            func_param_tp = (func_param_tp, )
        return func_name(self.handle_context, *func_param_tp)

    def check_ini_data(self):
        pass

