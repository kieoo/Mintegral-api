#!/usr/bin/python
# -*- coding: utf-8 -*-
#coding=utf-8
'''
Created on 2015年11月10日

@author: Linked
'''
import MySQLdb
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from features.dao import Session


class SqlTemplate(object):
        
    """
    @deprecated: 构造函数
    """
    def __init__(self, h='52.74.240.202', p=3306, u='root', pw='TNKq6de8ttjGq4aB', da='mob_adn'):
        try:
            self.connection = MySQLdb.connect(
                                    host=h,
                                    port=p,
                                    user=u,
                                    passwd=pw,
                                    db=da
                                )
            self.session = Session(autocommit=True)
        except Exception, e:
            print(e)
            raise e  # 构建对象失败，抛异常
    
    
    """
    @deprecated: 查询一条记录
    @author: Linked
    @since: 2015-11-11
    @param class_or_type_or_tuple: 查询的table对应的model持久化类
    @param param: 查询条件，dict类型
    @return: 返回一个class_or_type_or_tuple实例；如果结果不唯一，返回None
    """
    def selectOne(self, class_or_type_or_tuple, param):
        obj = None
        try:
            obj = self.session.query(class_or_type_or_tuple).filter_by(**param).one()
        except NoResultFound, e:
            print(e)
        except MultipleResultsFound, e:
            print(e)
        return obj
    
    
    
    
    """
    @deprecated: 查询多条记录
    @author: Linked
    @since: 2015-11-11
    @param class_or_type_or_tuple: 查询的table对应的model持久化类
    @param param: 查询条件，dict类型
    @return: 返回一个List<class_or_type_or_tuple>对象
    """
    def selectList(self, class_or_type_or_tuple, param):
        resultList = []
        try:
            resultList = self.session.query(class_or_type_or_tuple).filter_by(**param).all()
        except Exception, e:
            print(e)
        return resultList  
        
    
    
    """
    @deprecated: 插入一条记录
    @author: Linked
    @since: 2015-11-11
    @param obj: 新增的记录对应的model对象 
    @return: 成功返回1，失败返回0
    """
    def insert(self, obj):
        result = 0
        try:
            self.session.begin()
            self.session.add(obj)
            self.session.commit()
            result = 1
        except Exception, e:
            self.session.rollback()
            print e
        return result

    """
    @deprecated: 插入一条记录, 并返回sql插入的结果数据
    @author: qyke
    @since: 2017-11-14
    @param obj: 新增的记录对应的model对象 
    @return: 成功返回所有记录信息, 失败返回0
    
    """
    def insert_ex(self, obj, class_or_type_or_tuple, return_data=1):
        result = 0
        try:
            self.session.begin()
            self.session.add(obj)
            self.session.commit()
            result = 1
            if return_data:
                data_id = self.session.execute('SELECT LAST_INSERT_ID()').first()[0]
                user_info = self.selectOne(class_or_type_or_tuple, {'id': data_id})
                return user_info
        except Exception, e:
            self.session.rollback()
            print e
        return result
    
    
    """
    Create On 2015年11月11
    @deprecated: 更新记录
    @param class_or_type_or_tuple: 表对应的model层类
    @param param: 更新条件，dict类型
    @param data: 更新内容，dict类型
    @return: 成功返回1，失败返回0
    @author: Linked
    """
    def update(self, class_or_type_or_tuple, param, data):
        result = 0
        objList = []
        try:
            objList = self.session.query(class_or_type_or_tuple).filter_by(**param).all()
            self.session.begin()
            for obj in objList:
                for (key, value) in data.items():
                    setattr(obj, key, value)  #修改对象属性
            self.session.commit()
            result = 1
        except Exception, e:
            self.session.rollback()
            print e
        return result
    
    
    """
    Create On 2015年11月11
    @deprecated: 删除记录
    @param class_or_type_or_tuple: 表对应的model层类
    @param param: 删除条件，dict类型
    @return: 成功返回1，失败返回0
    @author: Linked
    """
    def delete(self, class_or_type_or_tuple, param):
        result = 0
        objList = []
        try:
            objList = self.session.query(class_or_type_or_tuple).filter_by(**param).all()
            self.session.begin()
            for obj in objList:
                self.session.delete(obj)
            self.session.commit()
            result = 1
        except Exception, e:
            self.session.rollback()
            print e
        return result
    
    
    def commit(self):
        self.session.commit()
        return 1
    
    def begin(self):
        self.session.begin()
        return 1
    
    def execute(self, sql):
        result = 0
        try:
            self.connection.query(sql)
            result = 1
        except Exception, e:
            print e
        return result
    
    
    def cleanCache(self):
        result = 0
        try:
            self.connection.query("truncate table cache")
            result = 1
        except Exception, e:
            print e
        return result        
        
        
######################## 高能区域 #############################################
# coding=utf-8
# conn= MySQLdb.connect(
#          host='52.74.240.202',
#          port = 3306,
#          user='root',
#          passwd='TNKq6de8ttjGq4aB',
#          db ='mob_adn'
#          )
# cur = conn.cursor()
# print cur.execute('desc advertiser_list')
# for c in cur:
#     print c
#     print type(c[0])
#    
# print 1
# for c in cur:
#     print c
#     print type(c[0])
# session = SqlTemplate()
# print(dir(session.connection))

