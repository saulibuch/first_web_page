# -*- coding: UTF-8 -*-
# trying to put whole file opening to one line. How shall I close the file object?
from sys import argv
from os.path import exists

script, from_file, to_file = argv 

in_file = open(from_file) 
indata = in_file.read()

out_file = open(to_file, 'w')
out_file.write(indata)

print ("Copy form %s to %s completed." % (from_file, to_file) )

in_file.close()
out_file.close()
