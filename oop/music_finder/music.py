import json
# create class
class Music():
	# init attr
	# think about array nested vs. hash
	def __init__(self, name, my_music, file_name):
		self.name = name
		self.my_music = my_music
		self.file_name = file_name
		self.friends = {}
		self.deleted_artists = []

	# Feature Level One
	def add(self):
		new_song = input(' What artist do you want to add')
		# add to end of list in json

		self.my_music[self.name].insert(-1,new_song)

		#self.my_music[self.name].append(new_song)
		# text based file
		# file = open(self.file_name, 'w')
		# file.write(str(self.my_music))
		# file.close()

		#json based ds
		with open(self.file_name, 'w') as outfile:
			json.dump(self.my_music, outfile)

	def remove(self):
		remove_song = input('what artist do you want to remove')
		#temporary trash save
		self.deleted_artists.append(remove_song)
		# remove item for value of dict
		for a in self.my_music.values():
			if remove_song in a:
				a.remove(remove_song)
			print(a)
		# text based file
		# file = open(self.file_name, 'w')
		# file.write(str(self.my_music))
		# file.close()
		# Write as an addition to current json
		with open(self.file_name, 'w') as outfile:
			json.dump(self.my_music, outfile)

	def list(self):
		fh = open(self.file_name)
		for line in fh:
			print(line)
		fh.close()

	# Feature level 2

	def list_friends(self):
		for x, y in self.friends.items():
			print("You and %s share %s"%(x, y))


	def list_deleted_artist(self):
		for x in self.deleted_artists:
			print(x)

	def add_friends(self):
		new_friend = input('who is your new friend?')
		new_friend_song = input('what band do you share?')
		self.friends[new_friend] = new_friend_song
		with open(self.file_name, 'a') as outfile:
				json.dump(self.friends, outfile)

	def find_friend(self, friend):
		friend_shared_artist = [element for element in self.my_music[self.name] if element in friend.my_music[friend.name]]
		friend_shared_artist = str(friend_shared_artist)[1:-1]
		if friend_shared_artist != '':
			print("You and %s have %s in common"%(friend.name, friend_shared_artist))
			like_music = {friend.name: friend_shared_artist}
			# get rid of double quote
			with open(self.file_name, 'a') as outfile:
				json.dump(like_music, outfile)


	def all_friends(self):
		pass


	# Level 3 Features


meow = Music('Estelle',{'Estelle': ['car seat headrest', 'king tuff']}, 'estelle.json')
bork = Music('Ben', {'Ben': ['car seat headrest', 'the rabbits']}, 'ben.txt')


while True:
	print("1: list")
	print("2: Add")
	print("3: Remove")
	print("4: Find Friends")
	print("5: Add Friend ")
	print("6: Remove Friends ")
	print("7: See All Friends")
	print("8: See Trash")
	userChoice = int(input())
	if userChoice is 1:
		print('')
		meow.list()
		print('')
	elif userChoice is 2:
		print('')
		meow.add()
		print('')
	elif userChoice is 3:
		print('')
		meow.remove()
		print('')
	elif userChoice is 4:
		print('')
		Music.find_friend(meow, bork)
	elif userChoice is 5:
		print('')
		meow.add_friends()
		print('')
	elif userChoice is 6:
		print('Coming Soon')
	elif userChoice is 7:
		print('')
		meow.list_friends()
		print('')
	elif userChoice is 8:
		print('')
		meow.list_deleted_artist()
		print('')
	else:
		exit()
