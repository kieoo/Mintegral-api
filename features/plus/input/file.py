#!/usr/bin/python
# -*- coding: utf-8 -*-
#coding=utf-8
'''
Created on 2015年12月4日

@author: Administrator
'''
from features.plus.input import Input


class File(Input):
    '''
    classdocs
    '''


    def __init__(self):
        pass
    
    """
    Create On 2015年12月4日
    
    @deprecated: 往file上传框输入内容value
    """
    @staticmethod
    def send_keys(driver, selector, unique_selector, value):
        element = File.find_element(driver, selector, unique_selector)
        #element.clear()
        element.send_keys(value)
        return element
    
    
   
        
        
        
        
        
        
        
        
        