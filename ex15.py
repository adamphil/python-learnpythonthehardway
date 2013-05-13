from sys import argv

# uses script as args[0] default
# filename is initial input
script, filename = argv

# stores opened filename in txt
txt = open(filename)

# prints filename with single quotes
print "Here's your file %r:" % filename
# prints filename contents (raw code)
print txt.read()

# prints string to request input
print "Type the filename again please:"
# stores user input into file_again
file_again = raw_input(">>> ")

# stores opened file_again in txt_again
txt_again = open(file_again)

# prints file_again contents
print txt_again.read()

# alternate shorthand call (skip txt_again)
# print open(file_again).read()

# close file instances
txt.close()
txt_again.close()