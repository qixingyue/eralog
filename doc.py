#!/bin/env python
#coding=utf-8

import sys
import json

methods_str = open("methods.json","r").read()
methods = json.loads(methods_str)

if len(sys.argv) >= 2:
	method = methods[sys.argv[1]]
	for key in method.keys():
		print key , ":" , method[key]
else :
	for key in methods.keys():
		print ""
		print "* " ,key
		method = methods[key]
		for key in method.keys():
			print "  >* " , key , ":" , method[key]

