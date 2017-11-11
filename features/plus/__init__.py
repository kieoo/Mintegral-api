#!/usr/bin/python
# -*- coding: utf-8 -*-
#coding=utf-8
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


BY_ID = 'id'
BY_CSS_SELECTOR = 'css_selector'
BY_TAG_NAME = 'tag_name'
BY_NAME = 'name'

class Element(object):
    def __init__(self):
        pass
    
    """
    Create On 2015年12月4日
    
    @deprecated: 定位浏览器上的元素，需要指定定位器以及唯一选择器
    @author: Linked
    """
    @staticmethod
    def find_element(driver, selector, unique_selector):
        if BY_ID == selector :
            element = driver.find_element_by_id(unique_selector)
        elif BY_CSS_SELECTOR == selector :
            element = driver.find_element_by_css_selector(unique_selector)
        elif BY_TAG_NAME == selector :
            element = driver.find_element_by_tag_name(unique_selector)
        elif BY_NAME == selector :
            element = driver.find_element_by_name(unique_selector)
        return element
    
    
    @staticmethod
    def click(driver, selector, unique_selector):
        element = Element.find_element(driver, selector, unique_selector)
        element.click()
        return element
    
    
    """
    Create On 2015年12月4日
    
    @deprecated: 将一个元素element拖动到另一个元素target
    @author: Linked
    """
    @staticmethod
    def drag_and_drop(driver, element, target):
        ActionChains(driver).drag_and_drop(element, target).perform()
    
    
    
    """
    Create On 2015年12月4日
    
    @deprecated: 清空元素的内容
    """
    @staticmethod
    def clear(driver, selector, unique_selector):
        pass
    
    
    
    @staticmethod
    def is_exist(driver, time, selector, unique_selector, message):
        if type(time) != int:
            time = int(time)
        if BY_ID == selector :
            WebDriverWait(driver, time).until(lambda x: x.find_element_by_id(unique_selector), message)
        elif BY_CSS_SELECTOR == selector :
            WebDriverWait(driver, time).until(lambda x: x.find_element_by_css_selector(unique_selector), message)
        elif BY_TAG_NAME == selector :
            WebDriverWait(driver, time).until(lambda x: x.find_element_by_tag_name(unique_selector), message)
        elif BY_NAME == selector :
            WebDriverWait(driver, time).until(lambda x: x.find_element_by_name(unique_selector), message)
    
    
    
    @staticmethod
    def is_displayed(driver, selector, unique_selector):
        pass
    
    
    @staticmethod
    def element_is_displayed(driver, time, selector, unique_selector, message=''):
        if type(time) != int:
            time = int(time)
        if BY_ID == selector :
            WebDriverWait(driver, time).until(lambda x: x.find_element_by_id(unique_selector).is_displayed() == True, message)
        elif BY_CSS_SELECTOR == selector :
            WebDriverWait(driver, time).until(lambda x: x.find_element_by_css_selector(unique_selector).is_displayed() == True, message)
        elif BY_TAG_NAME == selector :
            WebDriverWait(driver, time).until(lambda x: x.find_element_by_tag_name(unique_selector).is_displayed() == True, message)
        elif BY_NAME == selector :
            WebDriverWait(driver, time).until(lambda x: x.find_element_by_name(unique_selector).is_displayed() == True, message)
    
    
    @staticmethod
    def element_is_not_displayed(driver, time, selector, unique_selector, message=''):
        if type(time) != int:
            time = int(time)
        if BY_ID == selector :
            WebDriverWait(driver, time).until(lambda x: x.find_element_by_id(unique_selector).is_displayed() == False, message)
        elif BY_CSS_SELECTOR == selector :
            WebDriverWait(driver, time).until(lambda x: x.find_element_by_css_selector(unique_selector).is_displayed() == False, message)
        elif BY_TAG_NAME == selector :
            WebDriverWait(driver, time).until(lambda x: x.find_element_by_tag_name(unique_selector).is_displayed() == False, message)
        elif BY_NAME == selector :
            WebDriverWait(driver, time).until(lambda x: x.find_element_by_name(unique_selector).is_displayed() == False, message)
    
    
    
    
    """
    Create On 2015年12月07号
    
    @deprecated: 检查当前页面标题是否为title
    @author: Linked
    """
    @staticmethod
    def title_contains(driver, time, title, message=''):
        if type(time) != int:
            time = int(time)
        WebDriverWait(driver, time).until(expected_conditions.title_contains(title), message)
    
    
    """
    Create On 2015年12月07日
    
    @deprecated: 检测当前页面是否具有文本内容为text的元素
    @author: Linked
    """
    @staticmethod
    def element_contains_by_text(driver, time, selector, unique_selector, text, message=''):
        if type(time) != int:
            time = int(time)
        if BY_ID == selector :
            WebDriverWait(driver, time).until(lambda x: str(x.find_element_by_id(unique_selector).text) == str(text), message)
        elif BY_CSS_SELECTOR == selector :
            WebDriverWait(driver, time).until(lambda x: str(x.find_element_by_css_selector(unique_selector).text) == str(text), message)
        elif BY_TAG_NAME == selector :
            WebDriverWait(driver, time).until(lambda x: str(x.find_element_by_tag_name(unique_selector).text) == str(text), message)
        elif BY_NAME == selector :
            WebDriverWait(driver, time).until(lambda x: str(x.find_element_by_name(unique_selector).text) == str(text), message)
    
        
    
    
    
    
    