# Exercise 10-10: Common Words
# Download a public domain text from Project Gutenberg (https://gutenberg.org/)
# Save it as a .txt file in this directory.
# Use str.count() to count how many times the word 'the' appears.
# Tip: use .lower() before counting to catch 'The', 'THE', etc.

# TODO: Download a text file from Project Gutenberg and save it here
# TODO: Read the file and count occurrences of 'the' (case-insensitive)
with open('frankenstein.txt') as file_object:
    contents = file_object.read()
    count = contents.lower().count('the')
# TODO: Print the count
print(f"The word 'the' appears {count} times in Frankenstein.")
