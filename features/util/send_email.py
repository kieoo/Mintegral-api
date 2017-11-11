#!/usr/bin/python
# -*- coding: utf-8 -*-
#coding=utf-8
'''
Created on 2015年11月17日

@author: Administrator
'''

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#发送邮箱
sender = 'linked95@163.com'
#接收邮箱
receiver = 'liangkun.luo@mobvista.com'
#发送邮箱服务器
smtpserver = 'smtp.163.com'
#发送邮箱用户/密码
username = 'linked95@163.com'
password = 'zero20110509'
msgRoot = MIMEMultipart('related')
#邮件主题
msgRoot['Subject'] = 'Python email test'
#构造附件
att = MIMEText(open('E:\\ghostdriver.log', 'rb').read(), 'base64',
'utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment; filename="log.doc"'

msgRoot.attach(att)
smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(username, password)
smtp.sendmail(sender, receiver, msgRoot.as_string())
smtp.quit()
