# Exercise 8-8: User Albums
# Build on Exercise 8-7.
# Write a while loop that asks for album artist and title.
# Call make_album() and print the resulting dictionary.
# Include a quit value to exit the loop.

# TODO: Define make_album(artist, title) from exercise 8-7
def make_album(artist, title):
    return {
        'artist': artist,
        'title': title
    }


# TODO: Write a while loop asking for artist and title
while True:
    print("Tell me your favorite musician and their album")
    artist = input("Artist: ")
    album = input("Album: ")
    if artist == 'quit' or album == 'quit':
        break

    print(make_album(artist, album))
