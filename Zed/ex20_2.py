# -*- encoding=UTF-8 -*-

#load args functionality
from sys import argv

#name arguments
script, vlož_file = argv 

#function to print whole content of file object 
def print_all(f):
	print (f.read() )
#function to move position of"cursor" to the start od file object 
def rewind(f):
	f.seek(0)
#function to print number an current line of a file object 
def print_a_line(line_count, f):
	print (line_count, f.readline() )
#

#open file to file object
current_file = open(vlož_file)

print ("First let's print the whole file:\n")

#use of function to print whole file 
print_all(current_file)

print ("Now let's rewind, kind of like a tape.")

#move cursor again to the start of the file 
rewind (current_file)

print ("Let's print three lines:")

#set the counter to beginning
current_line = 1
#print first line, as cursor is at the beginning of the file 
print_a_line (current_line, current_file)

current_line += 1
#print second line, as this is the position nof cursor 
print_a_line (current_line, current_file)

current_line += 1
#print third line 
print_a_line (current_line, current_file)