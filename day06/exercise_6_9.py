# Exercise 6-9: Favorite Places
# Make a dictionary called 'favorite_places'.
# Use 3 names as keys; each value is a LIST of 1-3 favorite places.
# Loop through the dict and print each person's name and their favorite places.

# TODO: Create favorite_places dict where each value is a list of places
favorite_places = {
    'lisa': ['work', 'home', 'market'],
    'john': ['school', 'park'],
    'susan': ['cafe']
}
# TODO: Loop through and print each person's name and their places
for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places")
    for place in places:
        print(f"  {place.title()}")
