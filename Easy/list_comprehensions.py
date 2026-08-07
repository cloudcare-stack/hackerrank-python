'''
Task: You are given three integers: a, b, and c representing the dimensions of a cuboid along with an integer, n.

Print a list of all possible coordinates (a, b, c) on a 3D grid where the sum of a + b + c is not equal to n.
'''
a = int(input())
b = int(input())
c = int(input())
n = int(input())

# Create a list of all possible coordinates (i, j, k) where i + j + k is not equal to n
# Using a list comprehension by iterating through all possible values of i, j, and k within the ranges of a, b, and c respectively
# The expression of a list comprehension is: [expression for item in iterable if condition]
# We can use it without if condition to generate all combinations, and then filter out the ones that sum to n
result = [[i, j, k] for i in range(a + 1) for j in range(b + 1) for k in range(c + 1) if i + j + k != n]

# Print the resulting list
print(result)