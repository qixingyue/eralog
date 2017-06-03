#coding=utf-8

import client
import json

el = client.Eraylog({
	'basicAuth':{
		'username':'',
		'password':''
	}				
	,'protocol':'http'
	,'host':''
	,'port':12900
	,'path':''
});

same_params = {
	'query':'*'	
	,'filter':'streams:591034c9eb624a07e2a0910e'
	,'fields':'message'
	,'limit':3
}

cases = [

	{
		'params':{
			'from':'2017-05-24 00:00:00',
			'to':'2017-05-25 00:00:00',
		},
		'method':'searchAbsolute'
	},
	{
		'params':{
			'keyword':'one minute ago'
		},
		'method':'searchKeyword'
	},
	{
		'params':{
			'range':60
		},
		'method':'searchRelative'
	},
	{
		'params':{
			'field':'total_count',
			'interval':'minute',
			'keyword':'20 minute ago'
		},
		'method':'searchKeywordFieldHistogram'
	},
	{
		'params':{
			'from':'2017-05-24 00:00:00',
			'to':'2017-05-31 00:00:00',
			'field':'total_count',
			'interval':'day'
	   },
	   'method':'searchAbsoluteFieldHistogram'
	},
	{
		'params':{
			'fileld':'total_count',
			'interval':'minute',
			'range':3600
		},
		'method':'searchRelativeFieldHistogram'
	}


]

def doCase(case):
	global el
	global same_params
	params_ = same_params
	method = case['method']

	print "\n" + "= " * 15 + method + "= " * 15

	for k in case['params'].keys():
		params_[k] = case['params'][k]

	(message,bq,results,messages,total,time) = el(method,params = params_)

	if message != False:
		print "Error Found : " + message
	else :
		print "query in %d ms" % (time)
		print "total found %d " % (total)
		print "results : %s " % (json.dumps(results)) 
		print "messages : %s " % (json.dumps(messages)) 
		print "built query: %s " % (json.dumps(bq)) 


if __name__ == "__main__":
	for case in cases:
		doCase(case)
