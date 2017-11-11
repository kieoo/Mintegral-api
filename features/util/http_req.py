#!/usr/bin/python
# -*- coding: utf-8 -*-
#coding=utf-8
'''
@author: redstar
'''
import requests,time

_GET="get"
_POST="post"

class Request():
    
    def __init__(self,url,params={},headers={},method=_GET,verify=False,allow_redirects=False):
        self.url=url
        self.params=params
        self.headers=headers
        self.method=method
        self.verify=verify
        self.allow_redirects=allow_redirects
        self.response={
                       'http_status':None,
                       'body':{},
                       'headers':{}
                       }
        
    def __repr__( self ):
        return '<SendRequest %r %r %r %r>' % ( self.method, self.url, self.params, self.headers)

    def send_request(self,timeout=20.0,max_try = 3):
        timestamp = 0
        max_try = 3    
        while(max_try > 0):
            try:
                start = time.time()
                response = self.urlopen(timeout)
                timestamp = time.time() - start
            
                self.response['http_status'] = response.status_code
                self.response['headers'] = response.headers
                self.response['body'] = response.text
                break
        
            except :
                print "[Timeout]Got ReadTimeout Try Again..."
                max_try -= 1

        if max_try <= 0:
            raise  Exception("Send http request timeout! Retry failed!")
        
        print "[URL] %s\n[Http Status] %s\t[Time Stamp] %s " % (response.url,self.response['http_status'], timestamp)
        return self.response

    def urlopen(self,timeout):
        assert self.method in (_GET,_POST)
        
        if _GET==self.method:
            return requests.get(self.url, params=self.params, headers=self.headers, verify=self.verify, \
                                allow_redirects=self.allow_redirects,timeout=timeout)
        elif _POST==self.method:
            return requests.post(self.url, params=self.params, headers=self.headers, verify=self.verify, \
                                allow_redirects=self.allow_redirects,timeout=timeout)