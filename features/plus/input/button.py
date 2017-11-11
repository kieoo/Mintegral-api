#!/usr/bin/python
# -*- coding: utf-8 -*-
#coding=utf-8
'''
Created on 2015年12月4日

@author: Administrator
'''
from features.plus.input import Input


class Button(Input):
    '''
    classdocs
    '''


    def __init__(self, params):
        pass
    
    
    """
    Create On 2015年12月4日
    
    @deprecated: button按钮单击事件
    @author: Linked
    """
    @staticmethod
    def click(driver, selector, unique_selector):
        element = Button.find_element(driver, selector, unique_selector)
        element.click()
        return element
    
    
    """
    Create On 2015年12月4日
    
    @deprecated: 判断该button控件是否可视
    @return: 可视返回True；不可视返回False
    @author: Linked
    """
    @staticmethod
    def is_displayed(driver, selector, unique_selector):
        return Button.find_element(driver, selector, unique_selector).is_displayed()

    
    
    
