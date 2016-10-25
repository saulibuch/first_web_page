# importing argv variable to be able to read arguments from cmd line
from sys import argv

# unpacking arguments from cmd line, especially name of the file to read
script, filename = argv 

# reading content of file 
txt = open(filename)

# printing intro and file's name 
print ("Here's your file %r:" % filename )
# printing file's content 
print (txt.read() )

# asking and reading name of another file 
print ("Type the filename again:" )
file_again = input("> ")

#reading another file's content 
txt_again = open(file_again)

#printing another file's content 
print (txt_again.read() )