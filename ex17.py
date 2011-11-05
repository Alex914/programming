#This line imports a feature from the python feature set
#argv is the argument variable gives access to command line arguments
from sys import argv
#This imports a command named "exists" This returns "True" 
#if a file exists, "false" if not
from os.path import exists

#This defines the argument variable
script, from_file, to_file = argv

#This displays that we are copying from the first file to the second, and gives the names
print "Copying from %s to %s" % (from_file, to_file)

#we could do these two on one line too, how?
input = open(from_file)
indata = input.read()

#This prints the number of bytes long the first file is. len must calculate the length
#, indata is defined above as reading the input file
print "The input file is %d bytes long" % len (indata)

#"exists" must calculate if the to_file exists
print "Does the output file exist? %r" %exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
#This is just asking for a return to continue
raw_input()

#This defines the variable "output" as the opened "to_file". "w" means write
output = open(to_file, 'w')
#this takes the "indata" variable and writes it into output I guess?
output.write(indata)

print "Alright, all done."

#This closes the "output" file
output.close()
#This closes the "input" file
input.close()