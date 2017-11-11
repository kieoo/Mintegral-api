#!/usr/bin/python
# -*- coding: utf-8 -*-
#coding=utf-8
"""
Created on 2015年11月20日

@deprecated: 对文件操作的工具模块
@author: Linked
"""
from os.path import sys, os


"""
@deprecated: 获取当前文件的path
"""
def get_current_path():
    path = sys.path[0]
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)
