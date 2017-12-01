#!/usr/bin/python
# coding=utf-8

'''

Created on 2017年11月14日

@author: qyke

处理features用例数据 类

'''


import re
from features.util.func_util import *

func_re = re.compile(r'\$__fun\((?P<func_name>\w+),(?P<func_param>.*?)\)', re.I)
param_re = re.compile(r'\$\{(?P<save_key>[A-Za-z0-9_]+)\.{0,1}(?P<save_val>[A-Za-z0-9_]+){0,1}\}')


class HandleData(object):

    def __init__(self, context):
        self.datas_finish = context.text
        self.handle_context = context
        self.check_ini_data()  # TODO
        self.transfuc()
        self.transparam()

    def text_eval(self):
        try:
            datas_dict = eval(self.datas_finish)
        except Exception as e:
            print('Incorrect Dict Format=> ' + self.datas_finish)
            raise e
        return datas_dict

    def transfuc(self):
        """
            匹配context data中$__func()，拼装回text
        """
        trans_tmp = ''
        for data in self.datas_finish.split('\n'):
            ma = func_re.finditer(data)     # 匹配每行${}
            for func in ma:                 # 匹配行内每个${}
                func_list = func.groupdict()
                # func_value = self.func_exec(func_list['func_name'], func_list['func_param'])
                func_value = u'{0}({1},{2})'.format(func_list['func_name'], 'self.handle_context', func_list['func_param'])
                data = func_re.sub(str(func_value), data, 1)    # 每次替换一个$__func() 为 return
            trans_tmp += data + '\n'   # 拼装回text
        self.datas_finish = trans_tmp
        return

    def transparam(self):
        """
        匹配context data 中 ${}, 拼装回text
        :return:
        """
        trans_tmp = ''
        for data in self.datas_finish.split('\n'):
            ma = param_re.finditer(data)     # 匹配每行$__func()
            for param in ma:                 # 匹配行内每个$__func()
                param_list = param.groupdict()
                # param_value = self.func_exec('get_save_info',
                #                             '"'+param_list['save_name']+'","'+param_list['save_key']+'"')
                if param_list['save_key'] and param_list['save_val']:  # 匹配${a.b}
                    param_value = u'{0}({1},{2},{3})'.format('get_save_info', 'self.handle_context',
                                                             "'" + param_list['save_key'] + "'",
                                                             "'" + param_list['save_val'] + "'")
                else:  # 匹配${a}

                    param_value = u'{0}({1},{2},{3})'.format('get_save_info', 'self.handle_context', "'Tmp_Data'",
                                                         "'" + param_list['save_key']+"'")
                data = param_re.sub(str(param_value), data, 1)    # 每次替换一个${} 为 value
            trans_tmp += data + '\n'   # 拼装回text
        self.datas_finish = trans_tmp
        return

    def func_exec(self, name, param):
        from features.util import func_util
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

