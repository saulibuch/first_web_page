# -*- coding: UTF-8 -*-
# trying to put whole file opening to one line. How shall I close the file object?
from sys import argv
from os.path import exists

script, from_file, to_file = argv 

indata = open(from_file).read()
open(to_file, 'w').write(indata)

print ("Copy from %s to %s completed." % (from_file, to_file) )

