import json
# create class
class Music():
	# init attr
	# pass in data file per object, which is not the best way
    def __init__(self, name, my_music, file_name):
        self.name = name
        self.my_music = my_music
        self.file_name = file_name
        self.friends = {}
        self.deleted_artists = []

	# Feature Level One: Arrays
    def add(self):
        new_song = input(' What artist do you want to add')
        self.my_music.append(new_song)

    def remove(self):
        remove_song = input("what song do you want to remove")
        self.deleted_artists.append(remove_song)
        self.my_music.remove(remove_song)

    def list(self):
       for x in self.my_music:
           print(x)
# iterate through a hash
    def list_friends(self):
        for x, y in self.friends.items():
            print("You and %s share %s"%(x, y))
        print(self.friends)
# temporary save of deleted_artists
    def list_deleted_artist(self):
        for x in self.deleted_artists:
            print(x)
# add key/value to hash
    def add_friends(self):
       new_friend = input('who is your new friend?')
       new_friend_song = input('what band do you share?')
       self.friends[new_friend] = new_friend_song
# compare arrays + add to hash
    def find_friend(self, friend):
        friend_shared_artist = [element for element in self.my_music if element in friend.my_music]
        print(friend_shared_artist)
        if friend_shared_artist != " ":
            print("You and %s have %s in common"%(friend.name, friend_shared_artist))
            self.friends[friend.name] = friend_shared_artist
# expand for larger app. Compare array of all objects
    def all_friends(self):
        pass
# save data as json data
    def save(self):
        my_data = [self.my_music, self.friends]
        with open(self.file_name, 'w') as outfile:
            json.dump(my_data, outfile)

		# text based file
		# file = open(self.file_name, 'w')
		# file.write(str(self.my_music))
		# file.close()

# populate array of user info as json data or txt file

meow = Music('Estelle',['car seat headrest', 'king tuff',], 'estelle.json')
bork = Music('Ben', ['car seat headrest', 'the rabbits'], 'ben.txt')


while True:
    print("1: list")
    print("2: Add")
    print("3: Remove")
    print("4: Find Friends")
    print("5: Add Friend ")
    print("6: Remove Friends ")
    print("7: See All Friends")
    print("8: See Trash")
    print("9: save")

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
    elif userChoice is 9:
        print('')
        meow.save()
        print('')
    else:
        exit()
