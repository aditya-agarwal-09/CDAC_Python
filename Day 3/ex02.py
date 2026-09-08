playlist = input("Enter the movies in the playlist: ").split(',')

update = input("Enter the movie you want to add: ")

if(update in playlist):
    print("Already added!")
else:
    playlist.append(update)
    print(playlist)
