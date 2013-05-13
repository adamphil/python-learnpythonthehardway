# IMPORTANT FILE COMMANDS
# close: like File->Save
# read: reads contents of file
# readline: read just one line of text
# truncate: empties the file
# write(str): writes contents of str to file

from sys import argv

script, filename = argv

# Sugar to use default commands to guide user input
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

# Opens filename as an object with write permissions
print "Opening the file..."
target = open(filename, 'w') # alternates: r, a
# w+ opens in read and write mode

# Erases the contents of filename
print "Truncating the file. Goodbye!"

# Opening in w mode erases file contents by default
# target.truncate()

print "Now I'm going to ask you for three lines."

# Takes three lines of input
l1 = raw_input("line 1: ")
l2 = raw_input("line 2: ")
l3 = raw_input("line 3: ")

print "I'm going to write these to the file."

# Writes the three lines to file in longhand
'''
target.write(l1)
target.write("\n")
target.write(l2)
target.write("\n")
target.write(l3)
target.write("\n")
'''

# Alternate, shorthand write step
lines = l1 + "\n" + l2 + "\n" + l3
target.write(lines)

# Closes the filename object
print "And finally, we will close it."
target.close()

