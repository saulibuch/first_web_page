# importing argv module to read variables form cmd line
from sys import argv

# unpacking variables from cmd line
script, user_name = argv 
# setting  prompt for later use
prompt = '>  '

# printing intro
print ("Hi %s, I'm the %s script." % (user_name, script) )
print ("I'd like to ask you a few questions.")
# asking for self-likeness :)
print ("Do you like me %s?" % user_name) 
likes = input (prompt)

#asking for location of user 
print ("Where do you live, %s?" % user_name )
lives = input(prompt)

# asking for devise being run from 
print ("What kind of computer do you have?")
computer = input(prompt)

# combining gathered information, returning them to user 
print ( """
Alright, you you said %s about liking me.
You live in %s. Not sure where that is.
And you have a %s computer. Nice.
""" % (likes, lives, computer) )
