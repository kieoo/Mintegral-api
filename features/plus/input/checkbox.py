#!/usr/bin/env python
# -*- coding: utf-8 -*-
#coding=utf-8
'''
Created on 2015年12月7日

@deprecated: Checkbox控件接口类，用于对Checkbox进行操作
@author: Linked
'''
from features.plus import Element


class Checkbox(Element):

    def __init__(self):
        pass
    
    
    
    """
    @deprecated: Radio点击事件
    @return: 返回发生点击事件的Radio对象
    """
    @staticmethod
    def click(driver, selector, unique_selector):
        element = Checkbox.find_element(driver, selector, unique_selector)
        element.click()
        return element