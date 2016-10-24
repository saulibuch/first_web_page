#importing argv to be able to work with arguments of the script
from sys import argv

# assigneng read arguments to variables
script, first, second, third = argv

#printing out all the arguments passed to script
print ("The script is called:", script)
print ("Your first variable is:", first )
print ("Your seconf variable is:", second )
print ("You third variable is:", third )