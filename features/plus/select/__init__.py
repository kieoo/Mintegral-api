#!/usr/bin/python
# -*- coding: utf-8 -*-
#coding=utf-8
from features.plus import Element
from selenium.webdriver.support.select import Select as seSelect

class Select(Element):
    @staticmethod
    def select_by_text(driver, selector, unique_selector, text):
        element = Select.find_element(driver, selector, unique_selector)
        element = seSelect(element)
        element.select_by_visible_text(text)
        return element
    
    
    @staticmethod
    def select_by_index(driver, selector, unique_selector, text):
        element = Select.find_element(driver, selector, unique_selector)
        element = seSelect(element)
        element.select_by_index(text)
        return element