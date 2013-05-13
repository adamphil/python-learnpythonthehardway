from sys import exit

def start():
	print "You have appeared in a plaza."
	print "The walls, of gold; the floor, marble."
	print "You notice the arches above as you come fully to your senses."
	print "You are facing north.\n"
	print "What will you do?"

	facingNorth = True

	next = raw_input(">> ")

	if next == "walk":
		print "You arrive at a red door."
		print "What will you do next?"

		next_next = raw_input(">> ")

		if "open" in next_next:
			print "The door is locked. Initiate Plan B.\n"
			reset()
		else: 
			print "You return to the center of the room."
			reset()	

	if "west" in next:
		print "You see an ornate cabinet with a face of glass."

	else:
		boredom = """You stand in the center of the room so long that
you eventually die of excruciating boredom."""
		die(boredom)

def die(cause):
	print cause, "Nice going slick!"
	exit(0)

def reset():
	print "You vanish and reappear.\n"
	start()

start()