# prepare string, where I can insert any four other objects later
formatter = "%r %r %r %r"

# print the string with integers
print ( formatter % (1, 2, 3, 4 ) )
# and four strings
print ( formatter % ("onššše", "two", "three", "four" ) )
# and booleans
print ( formatter % (True, False, False, True) )
# and put it in itself
print ( formatter % (formatter, formatter, formatter, formatter ) )
# and foru strings, which are displayed ach on its own line for transparency
print ( formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
) )
