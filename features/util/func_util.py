#!/usr/bin/python
#coding=utf-8

'''
Created on 2017年11月14日

@author: qyke
'''

import hashlib
import random
import string


def get_user_info(cont, keys):

    info_list = []

    for key in keys:
        info_list.append(cont.user_model.get(key))

    return ','.join(info_list)


def get_random_string(cont, rlen=32):

    random_list = random.sample(string.ascii_letters + string.digits, rlen)  # 产生一个32长随机字符数组

    return ''.join(random_list)
