# =========================
# STRING FUNCTIONS / METHODS
# =========================

text = "Hello Python"

# Length
print(len(text))
# 12


# Change case
print(text.upper())
# HELLO PYTHON

print(text.lower())
# hello python

print(text.title())
# Hello Python

print(text.capitalize())
# Hello python


# Remove spaces
name = "  Colin  "

print(name.strip())   # removes both sides
print(name.lstrip())  # removes left side
print(name.rstrip())  # removes right side


# Replace
text = "I like Java"

print(text.replace("Java", "Python"))
# I like Python


# Split string into a list
text = "apple,banana,orange"

fruits = text.split(",")
print(fruits)
# ['apple', 'banana', 'orange']


# Join list into a string
words = ["Hello", "Python", "World"]

result = " ".join(words)
print(result)
# Hello Python World


# Find text
text = "Hello Python"

print(text.find("Python"))
# 6


# Count occurrences
text = "banana"

print(text.count("a"))
# 3


# Check beginning / ending
filename = "notes.txt"

print(filename.startswith("notes"))
# True

print(filename.endswith(".txt"))
# True


# String checking methods
text = "Python"

print(text.isalpha())   # True - letters only

number = "12345"

print(number.isdigit()) # True - digits only

value = "Python123"

print(value.isalnum())  # True - letters/numbers only


# Check if text exists
text = "I am learning Python"

if "Python" in text:
    print("Found Python")


# String indexing
word = "Python"

print(word[0])   # P
print(word[-1])  # n


# String slicing
print(word[0:3])
# Pyt

print(word[2:])
# thon

print(word[::-1])
# nohtyP