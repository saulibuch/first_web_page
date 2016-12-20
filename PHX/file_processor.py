# -*- coding: UTF-8 -*-

from sys import argv
import re
import sys

def ExtractData (string):
	'''Takes a line of text in predefined format and returns useful values.
	
	Expected format:
	[datum a čas][trvání][dálka vyzvánění][číslo agenta][ANI][DNIS][uživatelská data].wav
	
	Returns:
	- all parameters from string in parenthesis, arranged in array
	- callID 
	- date and time
	
	'''
	s1 = ParamPattern.findall(string)
	s2 = CallIDPattern.search(string).group(0)
	s3 = TimePattern.search(string).group(0)
	return s1, s2, s3
#
def ConvertTimeFormat (string):
	'''Converts time format from 2016-10-03_17-06-59 to 25.07.2016 01:01:01 '''
	data = re.findall('\d{2,4}', string)
	NewFormat = data[2]+'.'+data[1]+'.'+data[0]+' '+data[3]+':'+data[4]+':'+data[5]
	return NewFormat
#

def UpdateJson (Json, s1, s2, s3):
	'''replaces time and callID in a given json tempalte '''
	Jsonv2 = Json.replace('putTIMEhere', s1)
	Jsonv3 = Jsonv2.replace('putFILENAMEhere', s3)
	NewJson = Jsonv3.replace('putIDhere', s2)
	return NewJson
#
def SaveJsonFile (content, name):
	''' saves new json file with input text and name '''
	with open(name, 'w') as file:
		file.write(content)
#
def PrepareCommand (filename): 
	'''inserts name of file to tempalte command '''
	result = CurlSource.replace('putJSONNAMEhere', filename)
	return result 
#
def SaveCurls (list):
	'''saves all commands form list to file'''
	with open(curl_output, 'w') as file:
		for command in CurlList:
			file.write(command+'\n')
#
	
	

try:
	Script, Source_file, JsonTemplateFile, curl_output = argv #reads input files
except (ValueError):
	print('''
	file_processor.py requires 3 parametrs:
		- txt file with list of .wav input files; needs to have proper format
		- tempalte of json file
		- name of output files where all the resulting curl comamnds will be listed.
	''')
	sys.exit()

ParamPattern = re.compile('[\d_=\s\w-]+')
CallIDPattern = re.compile('(?<=CallID=)[\d\w]+')
TimePattern = re.compile('[0-9]{4}-[0-9]{2}-[0-9]{2}_[0-9]{2}-[0-9]{2}-[0-9]{2}')
with open(JsonTemplateFile) as file:  # reads template of json
	JsonTemplate = file.read()
#
with open(curl_output, 'w') as file: #clear list fo curl commands
	pass
#
print (curl_output)
with open('template_curl.txt', 'r') as file:  #read template of curl command
	CurlSource = file.readline()
#
CurlList = [] #prepare empty list for curl commands


with open(Source_file) as File:
	for Line in File:
		AllData, CallID , Time = ExtractData(Line) #takes 1 line of input file
		NewTime = ConvertTimeFormat (Time) # change time format
		JsonName = CallID+'.json' #prepare json file name based on call ID
		UpdatedJson = UpdateJson (JsonTemplate, NewTime, CallID, Line) #prepare json body
		SaveJsonFile(UpdatedJson, JsonName) # save json file
		CurlList.append(PrepareCommand (JsonName)) # add new command to list of all curl commands 
#
SaveCurls(CurlList)# save all curl commnads to file