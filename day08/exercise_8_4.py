# Exercise 8-4: Large Shirts
# Modify make_shirt() so large is the default size
#  and "I love Python" is the default message.
# Make a large shirt with the default message.
# Make a medium shirt with the default message.
# Make a shirt of any size with a different message.

# TODO: Define make_shirt(size='large', message='I love Python')
def make_shirt(size='large', message='I love Python'):
    print(f"I'll make a {size} shirt with the text: {message}.")


# TODO: Call it three times as described above
make_shirt(size='large', message='I love Python')
make_shirt(size='medium', message='I love Python')
make_shirt(size='small', message='I love Python')
