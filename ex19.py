# FUNCTIONS AND VARIABLES

def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that is enough for a party!"
	print "Get a blanket.\n"

print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)

print "OR, we can use variables from the script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def calculator(num1,num2,op):
	if op == '+':
		print "%d plus %d = %d" % (num1, num2, num1 + num2)
	if op == '-':
		print "%d minus %d = %d" % (num1, num2, num1 - num2)
	if op == '*':
		print "%d times %d = %d" % (num1, num2, num1 * num2)
	if op == '/':
		print "%d divided by %d = %d" % (num1, num2, num1/num2)

print "Here are some operations:"
calculator(5,10,'+')
calculator(5,10,'-')
calculator(5,10,'*')
calculator(5,10,'/')