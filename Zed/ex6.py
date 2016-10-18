# set up first sentence
x = "There are %d types of people." % 10
#adding suplementar words to be added to second sentence
binary = "binary"
do_not = "don't"
# set up second sentence, using formatted words
y = "Those who know %s and those who %s." % (binary, do_not)

# printing fist and second sentences
print (x)
print (y)

#printing repeating of two sentences; these are used as formatted text
print ("I said: %r." %x )
print ("I also said: '%s'." % y )

# creation word to be used as formatted text in third sentence; Boolean is used 
hilarious = False
# creating third sentence as parameters; formatting is used in sentence, even without adding formatted text at the same time
joke_evaluation = "Isn't that joke so funny?! %r"

# print the third sencetence - both sentence with formatting and formatted string is used as parameters 
print (joke_evaluation % hilarious )

# set up of fourth sentence, saving text in parameters
w = "This is a left side of..."
e = "a string with a right side."

# printing last sentence as a string concatenantion
print (w + e)