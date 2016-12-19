# -*- coding: UTF-8 -*-

from sys import argv
import re

Script, Source_file = argv

ParamPattern = re.compile('[\d_=\s\w-]+')
CallIDPattern = re.compile('(?<=CallID=)[\d\w]+')

with open(Source_file) as File:
	for Line in File:
		MyMatch = ParamPattern.findall(Line)
		CallID = CallIDPattern.search(Line).group(0)
		print (CallID)
		print (MyMatch[0])
