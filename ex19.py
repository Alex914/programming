# This line defines the function (cheese_and_crackers) and the
# arguments (cheese_count, boxes of crackers)
def cheese_and_crackers(cheese_count, boxes_of_crackers):
# This takes the number given for cheese_count and stickes it in for
# %d, which is a placeholder for integers
	print "You have %d cheeses!" % cheese_count
# This takes the number given for boxes_of_crackers and stickes 
# it in for %d, which is a placeholder for integers
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "an that's enough for a party!"
	print "Get a blanket.\n"


print "We can just give the function numbers directly:"
# This runs the functions and puts 20 and 30 in for cheese_count and 
# boxes_of_crackers
cheese_and_crackers(20, 30)


print "OR, we can use variables from our script:"
# These create variables and assign them values
amount_of_cheese = 10
amount_of_crackers = 50

# This runs cheese_and_crackers with the above definitions (and 
# their values) entered in for cheese_count and boxes_of_crackers
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
# This puts 10 + 20 in for the first argument and 5 + 6 in
# for the second
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, variables and math:"
# This subs in the above variables (amount of cheese and amount of 
# crackers) and does some math with them
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)