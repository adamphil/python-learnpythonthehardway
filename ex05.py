# -- coding: utf-8 --

name = 'Zed A. Shaw'
age = 35
height = 74 # inches 
zeight = 74 + 180
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d punds heavy." % weight
print "Actually %r thats not too heavy." % zeight
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

print "If I add %d, %d, and %d I get %d." % (
	age, height, weight, age + height + weight)

inches = 12.0
pounds = 10.0
centimeters = inches * 2.54
kilos = pounds * 0.453592

print "%d pounds equates to %f kilograms." % (pounds, kilos)
print "%d inches equates to %f centimeters." % (inches, centimeters)
