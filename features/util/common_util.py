#!/usr/bin/python
# -*- coding: utf-8 -*-
#coding=utf-8
"""
Created on 2015年11月06日
@deprecated: 通用方法包
@author: Linked
"""


from hamcrest.core import assert_that
from hamcrest.core.core import is_
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from features.config import login_account, module_title_mapping
from features.config.login_config import publisherDict
from features.model.publisher import Publisher
from features.plus import BY_CSS_SELECTOR
from features.plus import Element
from features.plus.input.button import Button
from features.util.func_util import matcher


def before_login(context):
	session = context.session
	publisher = Publisher()
	publisher.setPublisher(publisherDict)
	assert_that(session.delete(Publisher, {'id': publisher.id}), is_(1), u'delete data failure!')
	assert_that(session.delete(Publisher, {'email': publisher.email}), is_(1), u'delete data failure!')
	session.insert(publisher)
	
	

def login_step(context):
	before_login(context)
	driver = webdriver.PhantomJS()
# 	driver = webdriver.Firefox()
# 	driver.maximize_window()
	driver.get(login_account.get('page_url'))
	WebDriverWait(driver, 60).until(EC.title_contains(login_account.get('title')))  #检测是否访问到登录页面Login - Mobvista
	driver.find_element_by_id('email').send_keys(login_account.get('email'))
	driver.find_element_by_id('password').send_keys(login_account.get('password'))
	driver.find_element_by_id('login').click()
	WebDriverWait(driver, 60).until(EC.title_contains(module_title_mapping.get(u'登录')))
	return driver



def logout_step(driver):
	Button.find_element(driver, BY_CSS_SELECTOR, 'a[href="/user/logout"]').click()
	Element.title_contains(driver, 60, login_account.get('title'), u'注销失败！')



def object_to_dict(obj):
	return (obj == None and [obj] or [obj.__dict__])[0]



"""
Create On 2015年12月8日

@deprecated: 判断source的数据是否跟pattern一致
@param source: dict类型
@param pattern: dict类型
@return: True
"""
def is_matcher(source, pattern):
	if source == None or pattern == None:
		return False
	result = True
	for (k, v) in pattern.iteritems():
		if source.get(k) == None:
			return False
		if (type(source.get(k))(source.get(k))) != (type(source.get(k))(v)):
			result = False
			break
	return result

# source = {'a':1, 'b':2, 'c':3}
# pattern ={'b':2, 'a':1}		
# print is_matcher(source, pattern)



"""
@deprecated: 判断mongo数据是否满足配置表类型, 要求配置表与mongo字段一致
"""
def is_type_right(source, type_mapping):
	if source == None or type_mapping == None\
		or type(source) != dict or type(type_mapping) != dict:
		return False
	
	result = True
	for (k, v) in type_mapping.iteritems():
		if source.get(k) == None:
			continue
		if type(v) == dict:
			if is_type_right(source.get(k), v) == False:
				result =False
				break
		else:
			if v != type(source.get(k)):
				print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
				print(k)
				print(v)
				print(source.get(k))
				print(type(source.get(k)))
				print(source)
				print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
				result = False
				break
	return result

# mongo = MongoClient('52.74.240.202', 27017)
# source = mongo.get_database('new_adn').get_collection('campaign').find_one()
# print source
# for key, v in source.items():
# 	print key
# 	print type(v)
# print is_type_right(source, app_mongo_type)
# print(type(source.get('apikey')))


"""
@deprecated: 比较两个dict，不比较value的类型；用于mysql与页面数据比较
@author: Linked
"""
def matche_two_dict_ignore_case(left_source, right_source):
	if len(left_source) != len(right_source):
		return False
	result = True
	for key, value in left_source.items():
		if right_source.has_key(key) == False:
			return False
		
		if type(value) == dict:
			if matche_two_dict_ignore_case(left_source[key], right_source[key]) == False:
				result = False
				break
		elif type(value) == list:
			value.sort()
			right_source[key].sort()
			lens = len(left_source)
			for i in xrange(0, lens):
				if str(value[i]) != str(right_source.get(key)[i]):
					print("key: " + str(key) + " not equals!")
					print("\n")
					print("expected " + str(value[i]) + ", but was " + str(right_source.get(key)[i]))
					result = False
					break
			if result != True:
				break
		else:
			if str(value) != str(right_source.get(key)):
				print("key: " + str(key) + " not equals!")
				print("\n")
				print("expected " + str(value) + ", but was " + str(right_source.get(key)))
				result = False
				break
	return result
	
# a = {'a':[3,1,2], 'b':'2', 'c':{'c.c':1}}
# b = {'a':[1,2,'3'], 'b':2, 'c':{'c.c':'1'}}
# print matche_two_dict_ingore_case(a, b)


def matche_two_dict(left_source, right_source, source_mapping=None, mongo_type=None):
	print('##############matche_two_dict#########################')
	if source_mapping != None and mongo_type != None:
		result = True
		for k, v in source_mapping.items():
			print('key %s', k)
			if matcher(k, '.') != -1:	#处理二级嵌套
				karray = k.split('.')
				
				if mongo_type.get(karray[0]).get(karray[1]) == list:
					if right_source[v] == '':  #处理空串
						right_source[v] = []
					else:
						right_source[v] = right_source.get(v).split(',')
					for i in xrange(0, len(left_source.get(karray[0]).get(karray[1]))):
						left_source.get(karray[0]).get(karray[1])[i] = str(left_source.get(karray[0]).get(karray[1])[i])
				
				if mongo_type.get(karray[0])\
				.get(karray[1])(left_source.get(karray[0]).get(karray[1])) \
					!= mongo_type.get(karray[0]).get(karray[1])(right_source.get(v)):
					print(karray)
					print(mongo_type.get(karray[0]).get(karray[1]))
					print(left_source.get(karray[0]).get(karray[1]))
					print(right_source.get(v))
					result = False
					break
			else:
				if mongo_type.get(k) == list:
					if right_source[v] == '':
						right_source[v] = []
					else:
						right_source[v] = right_source.get(v).split(',')
					
					for i in xrange(0, len(left_source.get(k))):
						left_source.get(k)[i] = str(left_source.get(k)[i])
						
				if mongo_type.get(k)(left_source.get(k)) != mongo_type.get(k)(right_source.get(v)):
					print(k)
					print(left_source.get(k))
					print(type(left_source.get(k)))
					print(right_source.get(v))
					print(type(right_source.get(v)))
					result = False
					break
		return result
	else:
		return left_source == right_source

# a = {'a':'1', 'c.c':[1,2,{'cs':'2'}]}
# b = {'a':1, 'c.c':[1,2,{'cs':2}]}
# print matche_two_dict(a,b)
# 
# b.update(a)
# print b

# print str(a)
# mongo = MongoClient('52.74.240.202', 27017)
# left_source = mongo.get_database('new_adn').get_collection('app').find_one({'appId':22787})
# print(left_source)
# 
# session = sql_template.SqlTemplate()
# right_source = object_to_dict(session.selectOne(App, {'id':22787}))
# print(right_source)
# 
# print matche_two_dict(left_source, right_source, mongo_to_mysql_mapping)

			
# s = [242,153,245,250]
# print right_source.get('exclude_advertiser').split(',') == s
# ss = right_source.get('exclude_advertiser').split(',')
# for i in xrange(0, 4):
# 	print int(s[i]) == int(ss[i])
# 	
# s = 's'
# a= {'s':1}
# a[s] =2
# print a
		
# if random.randint(1, 10) >9:
#     application.exit()


# s = ''
# print s.split(',')


def dict_merge(distinct, source, is_only_cover = True):
	result = distinct.copy()
	if is_only_cover ==  True:  #覆盖
		for key, value in source.items():
			if distinct.has_key(key):
				result[key] = value
	else:  #合并，相同键取后值
		result.update(source)
	return result

# demo1 = {'a':1, 'c':5}
# demo2 = {'a':2, 'b':3}
# print dict_merge(demo1, demo2, False)


# 
# dict_demo.update(a=2)
# print dict_demo


"""
@deprecated: 将一个对象的所有属性转成int
"""
def str_to_int(source):
	if type(source) == list:
		les = len(source)
		for i in xrange(0, les):
			source[i] = str_to_int(source[i])
	elif type(source) == dict:
		for k, v in source.items():
			source[k] = int(v)
	else:
		source = int(source)
	return source

# a = ['1',['1'],{'a':'1'},1]
# print str_to_int(a)




def compare_page_and_mysql(page_data, mysql_data, page_info):
	rs = []
	for item in mysql_data:
		item = dict_merge(page_info, object_to_dict(item))
		rs.append(item)
	rs.sort()

	lens = len(rs)
	for i in xrange(0, lens):
		assert_that(matche_two_dict_ignore_case(rs[i], page_data[i]), is_(True), u'查询结果不匹配!')  #TODO:



def check_mysql_data(mysql_data, expect_mysql_data):
	result = 1
	for (k, v) in expect_mysql_data.iteritems():
		if mysql_data.has_key(k):
			if v != mysql_data.get(k):
				print(u'mysql_data key: ' + str(k) + u' not right!')
				print("expected " + str(v) + ", but was " + str(mysql_data.get(k)))
				result = 0
		else:
			print(u'mysql_data has not key: ' + str(k))
			result = 0
			break
	return result


def check_mongo_data(mongo_data, expect_mongo_data):
	result = 1
	for (k, v) in expect_mongo_data.iteritems():
		if mongo_data.has_key(k):
			if(type(v) == dict):
				if check_mongo_data(mongo_data.get(k), v) == 0:
					result = 0
					break
			elif v != mongo_data.get(k):
				print(u'mongo_data key: ' + str(k) + u' not right!')
				print("expected " + str(v) + ", but was " + str(mongo_data.get(k)))
				result = 0
				break
		else:
			print(u'mongo_data has not key: ' + str(k))
			result = 0
			break
	return result


