# Exercise 6-8: Pets
# Make several dictionaries, one for each pet.
# Each dict should have the kind of animal and owner's name.
# Store all dicts in a list called 'pets'.
# Loop through pets and print everything you know about each pet.

# TODO: Create multiple pet dictionaries with 'animal' and 'owner' keys
pet_1 = {'animal': 'dog', 'owner': 'lisa'}
pet_2 = {'animal': 'cat', 'owner': 'john'}
pet_3 = {'animal': 'bird', 'owner': 'lisa'}
pet_4 = {'animal': 'dog', 'owner': 'susan'}
pet_5 = {'animal': 'cat', 'owner': 'jack'}
# TODO: Store them in a list called 'pets'
pet_list = [pet_1, pet_2, pet_3, pet_4, pet_5]

# TODO: Loop and print each pet's info
for pet in pet_list:
    print(f"{pet['owner'].title()}'s pet is a {pet['animal']}.")
