@artists = ['sloth rust', 'sun flower bean' ]
@songs = ['7:30am', 'easier said than done' ]

def intro
	puts'welcome to the program. You can add or delete songs and artists'
end

def song_or_artist
	puts'would you like to work with songs or artist or list items: s/a/l'
	song_or_artist_user = gets.chomp

	if song_or_artist_user == 's'
		song_add_del
		puts @songs
	elsif song_or_artist_user == 'a'
		artist_add_del
		puts @songs
	elsif song_or_artist_user == 'l'
		list_all
	else
		song_or_artist
	end

	

end

def song_add_del
	puts'do you want to add or delete a song: a/d'
	song_mod = gets.chomp

	if song_mod == 'a'
		puts'what song do you want to add: '
		song_add = gets.chomp
		@songs.push(song_add)
	else
		puts'what song do you want to delete: '
		song_del = gets.chomp
		@songs.delete(song_del)
	end
end

def artist_add_del
	puts'do you want to add or delete a song: a/d'
	artist_mod = gets.chomp

	if artist_mod == 'a'
		puts'what song do you want to add: '
		artist_add = gets.chomp
		@artists.push(artist_add)
	else
		puts'what song do you want to delete: '
		artist_del = gets.chomp
		@artists.delete(artist_del)
	end
end

def list_all
	puts'do you want to see songs or artist list: s/a'
	list_mod = gets.chomp

	if list_mod == 'a'
		for x in @artists
			puts x
		end
	else
		for x in @songs
			puts x
		end
	end
	song_or_artist
end