#!/usr/bin/python
# -*- coding: utf-8 -*-
#coding=utf-8
from features.plus import Element, BY_ID, BY_CSS_SELECTOR, BY_TAG_NAME, BY_NAME


class Input(Element):
    def __init__(self):
        pass

    """
    Create On 2015年12月4日
    
    @deprecated: 清空text文本框的内容
    """
    @staticmethod
    def clear(driver, selector, unique_selector):
        element = Input.find_element(driver, selector, unique_selector)
        element.clear()
        return element