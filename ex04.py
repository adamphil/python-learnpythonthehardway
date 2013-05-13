#set car count
cars = 100
#set car capacity
space_in_a_car = 4.0
#drivers available
drivers = 30
#passengers available
passengers = 90
#cars not driven, or car count minus driver count
cars_not_driven = cars - drivers
#cars driven, equal to driver count
cars_driven = drivers
#carpool potential, amount of drivers times space left in a car
carpool_capacity = cars_driven * space_in_a_car
#average passengers is the passenger count divided amongst 
#the cars driven
average_passengers_per_car = passengers / cars_driven 

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be ", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

#extra underscore in "carpool_capacity" at line 13

#1. if its just 4, it can't be divided into decimals
#2. the amount of digits after the decimal is open and can float

#6
j = 4.5 * 3.2
k = 230 - 454 * 32 + 873 - 393
l = 478 / 45
m = j * k
n = k - (l / 2)
print m * (2 / n)

