#!/usr/bin/python
# -*- coding: utf-8 -*-
#coding=utf-8
'''
Created on 2015年12月7日

@deprecated: table标签操作类
@author: Linked
'''
from features.plus import Element

class Table(Element):
    def __init__(self):
        pass
    
    
    @staticmethod
    def find_thead(table):
        return table.find_element_by_tag_name('thead')
    
    
    @staticmethod
    def find_tbody(table):
        return table.find_element_by_tag_name('tbody')
    
    
    
    