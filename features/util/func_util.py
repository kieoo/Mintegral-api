#!/usr/bin/python
#coding=utf-8

'''
Created on 2017年11月14日

@author: qyke
'''

import hashlib
import random
import string


def get_user_info(context, keys):

    info_list = []

    if isinstance(keys, str):
        value = getattr(context.user_model, keys)
        return value

    for key in keys:
        value = getattr(context.user_model, key)
        info_list.append(value)

    return ','.join(info_list)


def get_random_string(context, rlen=32):

    random_list = random.sample(string.ascii_letters + string.digits, rlen)  # 产生一个32长随机字符数组

    return ''.join(random_list)
