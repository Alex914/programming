#: This symbol is used for making notes. Anything to the right of it will not run
as part of the program. For this reason you can use it to disable parts of code without
removing them

Example:

#print "Hello World" would not be displayed


print: This is used to display text or data to the user. To display text, put it in quotes
after print. Info can also be used instead of text, without the quotes.

Example:

print "Hens", 25 + 30 / 6

,: This symbol is used for separating values. It seems like sometimes it has a space after
and sometimes it does not.

Example:

print "Hens", 25 + 30 / 6


+-*/: These characters add, subtract, multiply, and divide. Duh.

Example:

print 2 + 2


< > =< =>: These characters are less than, greater than, less than or equal to, greater
than or equal to. If you use one of these, it will check whether it is true or false.

Example:

print 5 > 2 

would print "True"

=: This defines variables, allowing a value to be put to a name.

Example:
this_variable = 100
print this_variable

would display 100

.: A period is used to denote a floating point number, as apposed to an integer. 

Example:

print 3 / 2 would display 2
print 3.0 / 2 would display 1.5

"": Double quotes denote a string. Text and numbers can be put in strings, and they
don't act like integers. So "5" + "2" would yield 52. 

Example: 

w = "This is the left side of..."
e = "a string with a right side."

print w + e

print "." * 10


%: Variables are embedded using a 
specialized format (called, actually, a "format". You put a % in the string (followed by s for string or d for integer 
(I think) and then a % at the end with the variables in order they appeared in the 
string they are supposed to go in.

Example:
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)
    
    
(,): Parentheses and commas. When embedding variables in a string ("format", see above), 
sometimes you might want to embed multiple variables. When you do this, after the string you
would put the % character followed by the variables in a list within parentheses, separated
by commas.

Example: y = "Those who know %s and those who %s." % (binary, do_not)
   
   
n\: This makes a return when printing a string

Example:

months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the months: ", months


\t: This tabs in things to the right of it in a string

Example:

print "\tI'm tabbed in."



\: This is an "escape" for a quotes in a string. That means it prints the quote
instead of recognizing the quote as the end of a string.

Example:

"I am 6'2\" tall."
'I am 6\'2" tall.'
"\\"

""" """: displays blocks of text without having to to mark returns with a n\:

Example:

"""This text
and this text 
and this text"""


,: Commas are put at the end of print lines so they won't end the line with a newline and 
go to the next line.


raw_input(): When a variable is defined as raw_input(), when you run the code it will
prompt the user to input text. The text will then be used as that variable. Text in the
parenthesis (in quotation marks) will display that text as a prompt. Don't forget to put a 
space befor the end of the parethisis or else it will look weird.
Example:

print "How old are you?",
age = raw_input("age= ")

print "So, you're %r old" % (age)


from sys import argv: This script imports features from the python feature set. 

argv: This is the argument variable. This variable holds the argument you pass to the 
python script when you run it. I think this allows you to take text put in the command
line and use it in the script. So for example you would runt python doc1.py Whatever 
in the command line and this would put "Whatever" in the script when you assign argv 
to a variable. You can use multiple variables, and the variable "script" will give the
name of the script (the document file name).


open: This opens a file. Put the file name in the parenthesis, like this: 

open(filename.txt)

You can assign this to a variable, and then run a function on that variable, like this:

txt = open(filename.txt)
print txt.read.()

Run it with the parameter "w" (as in open(w)) to make it writeable.


file commands: File commands are commands run on files within a script. So you could
assign a file to a variable:

txt = open(filename.txt)

and then run commands on that variable. Commands are run by following the variable
with a period, the name of the command, and the parameters in parenthesis, with no
spaces. Empty parentheses mean no parameters. Don't forget to close() files, as
it is important to close them!

Example:

txt = open(filename.txt)
print txt.read()


close: Closes the file, with changes made. This is a file command.
read: Reads the contents of the file, and then you can assign the results to a variable.
This is a file command.
readline: This reads just one line of a text file. I think you put the line number in 
the paretheses. This is a file command.
truncate: Empties the file. This is a file command.
write(stuff): Writes stuff to the file. This is a file command.
seek: Put the line number in the parenthesis to goto this line of an open file.

from os.path import exists: The exists argument, when used as a function in the script,
returns true if a file does exist and false if it does not.

Example:

from sys import argv
from os.path import exists

file = argv
print "Does the output file exist? %r" % exists(file)

len: This returns the length of an open and read document when used as a variable. 

Example:

input = open(file.txt)
indata = input.read()
print "The input file is %d bytes long" % len(indata)

def: Defines a function. These name pieces of code the way variables name strings and numbers.
They take arguments the way your scripts take argv. This way instead of writing code
over and over again, you can define it once and then just call it up! Note that it ends
with a colon, and the next line is indented. Variables in functions are not connected 
to variables in the script. You can feed it numbers or variables.

Example:

def print_one(arg1):
    print "arg1: %r" % arg1
    
print_one("Stuff!")

FUNCTION CHECKLIST!:

    Did you start your function definition with def?
    Does your function name have only characters and _ (underscore) characters?
    Did you put an open parenthesis ( right after the function name?
    Did you put your arguments after the parenthesis ( separated by commas?
    Did you make each argument unique (meaning no duplicated names).
    Did you put a close parenthesis and a colon ): after the arguments?
    Did you indent all lines of code you want in the function 4 spaces? No more, no less.
    Did you "end" your function by going back to writing with no indent 
    (dedenting we call it)?

And when you run (aka "use" or "call") a function, check these things:

    Did you call/use/run this function by typing its name?
    Did you put ( character after the name to run it?
    Did you put the values you want into the parenthesis separated by commas?
    Did you end the function call with a ) character.

+=: Shorthand for add the first thing to the second and then define it as that 
result. 

Example:

a = 5
a += 1

print a

would print 6 because a now equals 6.

return: Used in a definition of a function, this allows you to use the function
as a variable equal to whatever it returns.
