#!/usr/bin/python
# coding=utf-8

'''

Created on 2017年11月14日

@author: qyke

处理输入数据

'''

import re

func_re = re.compile(r'\$__fun\((?P<func_name>\w+),(?P<func_param>.*?)\)')

class HandleDate(object):

    def __init__(self, context):
        self.datas_original_str = context.text
        self.datas_rel = ''
        self.transfuc()
        self.handle_context = context

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

    def func_exec(self, name, param):
        """
            执行context data中$__func()，返回values
            :type name: string, function name
            :type param: list, param
            :rtype : string
        """
        func_name = name
        func_param_list = param.split(',')

        return func_name(cont=self.handle_context, *func_param_list)
