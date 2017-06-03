#coding=utf-8

import requests
import base64
import json
import urllib

class Base:
	pass

"""
methods.json 来自于 https://www.npmjs.com/package/graylog-api
node-modules/graylog-api/api-methods.js
https://github.com/kolomiichenko/graylog-api
"""
method_str = open("methods.json","r").read()
methods = json.loads(method_str)

class Eraylog :

	def __init__(self,config):
		self._protocol = 'http' if 'protocol' not in config else  config['protocol']
		self._auth = '' if 'basicAuth' not in config else config['basicAuth']
		self._host = 'localhost' if 'host' not in config else config['host']
		self._port = 9200 if 'port' not in config else config['port']
		self._path = '' if 'path' not in config else config['path']
		self._uri = "%s://%s:%d%s" % (self._protocol,self._host,self._port,self._path)
		auth_str = "%s:%s" % (self._auth['username'],self._auth['password'])
		self._headers = {
				"Accept":"application/json",
				"Content-Type":"application/json",
				"Authorization": "Basic %s" % (base64.b64encode(auth_str))
		}

	def computedPath(self,path,params):
		if params != False and len(params.keys()) > 0 :
			rpath = path
			for p in params.keys():
				k = '{' + p + '}'
				rpath = rpath.replace(k,params[p])
			return rpath
		else :
			return path

	def wrapperResponse(self,response):
		ro = json.loads(response.text)
		if isinstance(ro,list):
			return (None,ro,None)

		built_query = False if 'built_query' not in ro else ro['built_query']
		results = False if 'results' not in ro else ro['results']
		messages = False if 'messages' not in ro else ro['messages']
		message = False if 'message' not in ro else ro['message']
		total_results = False if 'total_results' not in ro else ro['total_results']
		time = False if 'time' not in ro else ro['time']

		return (message,built_query,results,messages,total_results,time)

	
	def __call__(self,name,**args):
		global methods
		if name not in methods:
			return False

		method = methods[name]
		path = method['path']

		params = False if 'params' not in args else args['params']
		path_params = False if 'path' not in args else args['path']

		method_str = method['method']

		reqUri = self._uri + self.computedPath(path,path_params) 
		body = ""

		if method_str == 'GET' and params != False:
			reqUri = reqUri + '?' + urllib.urlencode(params)

		if method_str != 'GET' and params != False:
			body = json.dumps(params)

		if method_str == 'GET':
			response = requests.get(reqUri,headers = self._headers)
			return self.wrapperResponse(response)
			
		elif method_str == 'POST':
			pass
		elif method_str == 'DELETE':
			pass
		elif method_str == 'PUT':
			pass


