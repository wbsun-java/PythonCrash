# Chapter 2 — Variables and Simple Data Types
# Key examples from the book

# --- Variables ---
message = "Hello Python Crash Course reader!"
print(message)

message = "Hello Python world!"   # variable value can change
print(message)

# --- String methods ---
name = "ada lovelace"
print(name.title())   # Ada Lovelace
print(name.upper())   # ADA LOVELACE
print(name.lower())   # ada lovelace

# --- Concatenation ---
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print("Hello, " + full_name.title() + "!")

# --- Whitespace in strings ---
print("\tPython")           # tab
print("Languages:\nPython\nC\nJavaScript")   # newlines

# --- Stripping whitespace ---
favorite_language = ' python '
print(favorite_language.rstrip())   # strip right
print(favorite_language.lstrip())   # strip left
print(favorite_language.strip())    # strip both

# --- Numbers ---
print(2 + 3)    # 5
print(3 ** 2)   # 9  (exponent)
print(3 / 2)    # 1.5
print(3 // 2)   # 1  (floor division)

# --- str() to avoid TypeError ---
age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)

# --- Comments ---
# This is a comment — Python ignores it
print("Hello Python people!")

# --- Zen of Python ---
import this
