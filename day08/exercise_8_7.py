# Exercise 8-7: Album
# Write a function called make_album() that takes artist name and album title.
# Return a dictionary with those two pieces of info.
# Add an optional 'tracks' parameter — if provided, add it to the dict.
# Call it at least 3 times (at least once with tracks), and print each result.

# TODO: Define make_album(artist, title, tracks=None)
def make_album(artist, title, tracks=None):
    album = {'artist': artist, 'title': title}
    if tracks:
        album['tracks'] = tracks
    return album


# TODO: Call at least 3 times and print the returned dicts
album1 = make_album(
    artist='Pink Floyd',
    title='The Dark Side of the Moon'
)
album2 = make_album(
    artist='The Beatles',
    title="Sgt. Pepper's Lonely Hearts Club Band",
    tracks=13,
)
album3 = make_album(
    artist='Led Zeppelin',
    title='Led Zeppelin IV'
)
print(album1)
print(album2)
print(album3)
