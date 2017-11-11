#!/usr/bin/python
# -*- coding: utf-8 -*-
#coding=utf-8
'''
Created on 2015年12月7日

@deprecated: tr标签操作类
@author: Linked
'''
from features.plus.table import Table


class Tr(Table):
    def __init__(self):
        pass
    
    
    @staticmethod
    def find_td(tr):
        return tr.find_elements_by_tag_name('td')[0]
    
    
    @staticmethod
    def find_tds(tr):
        return tr.find_elements_by_tag_name('td')
    
    
    