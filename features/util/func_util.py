#!/usr/bin/python
# -*- coding: utf-8 -*-
#coding=utf-8
'''
Created on 2015年11月23日
@deprecated: 朴素的匹配算法
@return: 返回匹配到的字符串的首索引；如果匹配失败，则返回-1
@author: Linked
'''
def matcher(dest, patt):
    result = -1
    n = len(dest)
    m = len(patt)
    for s in xrange(0, n-m+1):
        if patt == dest[s:s+m]:
            result = s
            break
    #print('Pattern %s occurs with shift %d in %s' % (patt, result, dest))
    return result

#matcher(u'上海自来水来自海上海', u'上海')

# disc = 'fa fa-android'
# lens = len(disc)
# for s in xrange(0, lens-6):
#     if 'android' == disc[s:7+s]:
#         print('good')
