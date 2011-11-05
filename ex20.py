#this gives access to command line arguments
from sys import argv

#This defines the argument variable
script, input_file = argv

#This defines the print_all function. I think f is for the file?
def print_all(f):
	print f.read()

#This definses the rewind function. f.seek(0) must seek the first line	
def rewind (f):
	f.seek(0)
		
#This defines the print_a_line function. Line_count is equal to 
#current_line (which below increases by one each time), f.readline must read
#the line of the current_file. 

def print_a_line(line_count, f):
	print line_count, f.readline()
	
#this defines current_file, as the open file that was input at the
#beginning of the program.
current_file = open(input_file)
	
print "First let's print the whole file\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)