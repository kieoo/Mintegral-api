#!/usr/bin/python
# -*- coding: utf-8 -*-
#coding=utf-8
'''
Created on 2015年12月7日

@deprecated: tbody标签操作类
@author: Linked
'''
from features.plus.table import Table

class Tbody(Table):
    def __init__(self):
        pass
    
    
    @staticmethod
    def find_tr(tbody):
        return tbody.find_elements_by_tag_name('tr')[0]
    
    
    @staticmethod
    def find_trs(tbody):
        return tbody.find_elements_by_tag_name('tr')
    
    
    
    