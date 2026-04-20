# Exercise 2-7: Stripping Names
# Store a person's name with whitespace characters (\t and \n) at the beginning and end.
# Print the name once with whitespace visible.
# Then print using lstrip(), rstrip(), and strip().

name = "\t\n  Ada Lovelace  \n\t"

print("Original:       '" + name + "'")
print("Using rstrip(): '" + name.rstrip() + "'")
print("Using lstrip(): '" + name.lstrip() + "'")
print("Using strip():  '" + name.strip() + "'")
