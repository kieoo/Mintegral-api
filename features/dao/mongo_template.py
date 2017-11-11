#!/usr/bin/python
# -*- coding: utf-8 -*-
#coding=utf-8
'''
Created on 2015年11月10日
@deprecated: Mongo数据库接口类
@author: Linked
'''
from pymongo import MongoClient

class MongoTemplate(object):
    
    #TODO:方法参数类型检查

    def __init__(self, host="52.74.240.202", port=27017, db='new_adn'):
        try:
            self.mongo = MongoClient(host, port)
            self.db = db
        except Exception, e:
            print(e)
            raise e
    
    
    """
    Create On 2015年11月12日
    @deprecated: 查询指定集合中的符合条件的文档，返回一个文档对象
    @param collection: 查询集合
    @param param: 查询条件，dict类型
    @return: 返回查询结果，dict类型；如果查询结果为空，返回None
    """
    def findOne(self, collection, param):
        db = self.mongo.get_database(self.db)
        collection = db.get_collection(collection)
        return collection.find_one(param)
    
    
    """
    Create On 2015年11月12日
    @deprecated: 查询多个文档
    @param collection: 查询集合
    @param param: 查询条件 
    @return: 返回查询结果集，List<dict>类型
    """
    def find(self, collection, param):
        db = self.mongo.get_database(self.db)
        collection = db.get_collection(collection)
        return collection.find(param)
    
    
    """
    Create On 2015年11月12日
    @deprecated: 更新指定集合中符合条件的一个文档
    @param collection: 指定要查询的集合
    @param param: 更新条件  
    @param data: 更新内容
    @return: 更新成功返回1；更新失败返回0
    """
    def updateOne(self, collection, param, data):
        db = self.mongo.get_database(self.db)
        collection = db.get_collection(collection)
        result = collection.update_one(param, data, upsert=False)
        return result.modified_count
    
    
    """
    Create On 2015年11月12日
    @deprecated: 更新指定集合中所有符合条件的文档
    @param collection: 指定要查询的集合
    @param param: 更新条件  
    @param data: 更新内容
    @return: 更新成功返回！0，即更新操作修改的文档数；更新失败返回0
    """
    def update(self, collection, param, data):
        db = self.mongo.get_database(self.db)
        collection = db.get_collection(collection)
        result = collection.update_many(param, data, upsert=False)
        return result.modified_count
    
    
    """
    Create On 2015年11月12日
    @deprecated: 删除指定集合中符合条件的一个文档
    @param collection: 指定要查询的集合
    @param param: 更新条件  
    @return: 删除成功返回1；删除失败返回0
    """
    def deleteOne(self, collection, param):
        db = self.mongo.get_database(self.db)
        collection = db.get_collection(collection)
        result = collection.delete_one(param)
        return result.deleted_count
    
    
    """
    Create On 2015年11月12日
    @deprecated: 删除指定集合中所有符合条件的文档
    @param collection: 指定要查询的集合
    @param param: 更新条件  
    @return: 删除成功返回删除数量；删除失败返回0
    """
    def delete(self, collection, param):
        db = self.mongo.get_database(self.db)
        collection = db.get_collection(collection)
        result = collection.delete_many(param)
        return result.deleted_count
    
    
    """
    Create On 2015年11月12日
    @deprecated: 新增一个文档
    @param collection: 指定要查询的集合
    @param param: 新增文档
    @return: 返回id
    """
    def insertOne(self, collection, data):
        db = self.mongo.get_database(self.db)
        collection = db.get_collection(collection)
        result = collection.insert_one(data)
        return result.inserted_id
    
    
    """
    Create On 2015年11月12日
    @deprecated: 新增多个文档
    @param collection: 指定要查询的集合
    @param param: 更新条件
    @return: 返回id数组
    """
    def insert(self, collection, datas):
        db = self.mongo.get_database(self.db)
        collection = db.get_collection(collection)
        result = collection.insert_many(datas)
        return result.inserted_ids
    
    




    