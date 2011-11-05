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


<>=<=>: These characters are less than, greater than, less than or equal to, greater
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







