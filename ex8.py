#Assigns variable as four formatters
formatter = "%r %r %r %r"

#Prints four set of four placeholder formatters formatted with 1 2 3 4
print formatter % (1, 2, 3, 4)

#Prints placeholder filled with one two three and four
print formatter % ('one', 'two', 'three', 'four')

#Prints placeholder filled with boolean values
print formatter % (True, False, False, True)

#Prints placeholder filled with four instances of the placeholder
#In total, 16 "%r" are printed
print formatter % (formatter, formatter, formatter, formatter)

#Prints placeholder filled with four different strings
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)