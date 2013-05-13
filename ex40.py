class Song(object):

	# init takes self as args[0] always
	def __init__(self, lyrics):
		self.lyrics = lyrics

	# Custom function printing each line of lyrics in the Song object	
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

# Create Song object with bday lyrics and break into 3 lines to be read
happy_bday = Song(["Happy birthday to you",
					"I don't want to get sued",
					"So I'll stop right there"])


# Create Song object broken into 2 line song to also be read
bulls_on_parade = Song(["They rally around the family",
						"With pockets full of shells"])

# Call sing_me_a_song function on happy_bday variable
happy_bday.sing_me_a_song()
# Call sing_me_a_song function on bulls_on_parade variable
bulls_on_parade.sing_me_a_song()
