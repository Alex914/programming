#This defines a function, and the two variables associated with it
def add(a, b):
	print "ADDING %d + %d" % (a, b)
	#return makes it so that when this funciont is called later
	#(see line 23), it can be used as an argument in another function
	return a + b
	
def subtract (a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b
	
def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b
	
def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b
	
	
print "Let's do some math with just functions!"

age  = add(30, 5)
#See that above? add is a function but it is being used like a variable
height = subtract(78,4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# a puzzle for the extra credit, type it in anyway
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"

