#!/usr/bin/env python
# -*- coding: utf-8 -*-
#auth@binfang.ye
import urllib
import urllib2
import json


def login_action(usercode,password):
	url = 'http://isite.yindatech.com:8833/iSite/phone3_6!login.action?'
	getData = urllib.urlencode({'username':usercode,
							  	'password':password,
							  	'pt':'i',
							  	'device':'iphone'})	
	req = urllib2.Request('%s%s' %(url,getData))
	req.add_header('User-Agent' , 'iSite 3.602 (iPhone; iPhone OS 8.1; zh_CN)')
	try:
		resp = urllib2.urlopen(req,timeout=10)
		html = resp.read()
		#print resp
		s = json.loads(html)
		user_key = s['data']['key']
		print s['data']['username'] + " login successfully!"
		return user_key
	except urllib2.HTTPError, e:
		print  "Server Return Error Code %s" %e.code

def QDNearSite_action(longitude,latitude):
	user_key = login_action(usercode,password)
	url = 'http://isite.yindatech.com:8833/iSite/phone3_6!QDNearSite.action?'
	getData = urllib.urlencode({'key':user_key,
							  'longitude':longitude,
							  'latitude':latitude,
							  'pname':defaultProject,
							  'pid':defaultProjectID,
							  'department':defaultDepartment,
							  'departmentID':defaultDepartmentID})

def getQDContent_action(user_key):
	url = 'http://isite.yindatech.com:8833/iSite/phone3_1!getQDContent.action?'
	getData = urllib.urlencode({'key':user_key})
	req = urllib2.Request('%s%s' %(url,getData))
	req.add_header('User-Agent' , 'iSite 3.602 (iPhone; iPhone OS 8.1; zh_CN)')
	try:
		resp = urllib2.urlopen(req,timeout=10)
		html = resp.read()
		print html
	except urllib2.HTTPError, e:
		print  "Server Return Error Code %s" %e.code

def QianDao_action(user_key,bid,longitude,latitude,address,content,device,deviceID):
	url='http://isite.yindatech.com:8833/iSite/phone3_6!QianDao.action?'
	getData=urllib.urlencode({'key':user_key,
							  'bid':bid,
							  'longitude':longitude,
							  'latitude':latitude,
							  'address':address,
							  'content':content,
							  'device':device,
							  'deviceID':deviceID})

	req = urllib2.Request('%s%s' %(url,getData))
	req.add_header('User-Agent' , 'iSite 3.602 (iPhone; iPhone OS 8.1; zh_CN)')
	try:
		resp = urllib2.urlopen(req,timeout=10)
		html = resp.read()
		info = json.loads(html)['info']
		return info
	except urllib2.HTTPError, e:
		print  "Server Return Error Code %s" %e.code

def getBaseListByPid_action():
	pass


def sedn_sms(sender,passwd,receiver,message):
	url = 'https://quanapi.sinaapp.com/fetion.php?'
	getData = urllib.urlencode({'u':sender,'p':passwd,'to':receiver,'m':message})

	req = urllib2.Request('%s%s' %(url,getData))
	try:
		resp = urllib2.urlopen(req,timeout=10)
		html = resp.read()
		print html
	except urllib2.HTTPError, e:
		print  "Server Return Error Code %s" %e.code


if __name__ == '__main__':
	usercode = ''
	password = ''
	user_key = login_action(usercode,password)
	#getQDContent_action(user_key)
	bid       = 30774
	longitude = '121.551642'
	latitude  = '29.879912'
	address   = '浙江省宁波市海曙区月湖街道中山西路138号（移动海曙分公司）'
	content   = 'LTE后台'
	device    = 'iphone'
	deviceID  = '057A7BDB-D460-43C2-8D7D-F0AF059556B7'
	message   = address.decode('utf-8') + QianDao_action(user_key,bid,longitude,latitude,address,content,device,deviceID)
	print message
	sender    = ''
	passwd    = ''
	receiver  = ''
	sedn_sms(sender,passwd,receiver,message)





