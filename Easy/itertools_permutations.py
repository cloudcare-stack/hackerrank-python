'''
Task: Given a list of elements, write a Python function that returns all possible permutations of the elements in the list using the itertools module.

'''

from itertools import permutations

string, length = input().split()

for item in permutations(sorted(string), int(length)):
    print(''.join(item))