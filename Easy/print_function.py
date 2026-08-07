'''
Task: The included code stub will read an integer, n, from STDIN. Without using any string methods, try to print the following:
123...n
Note that "..." represents the consecutive values in between.
'''

n = int(input())

# # Use a loop to print numbers from 1 to n without spaces or newlines
# for i in range(1, n + 1):
#     print(i, end="")

# Store the numbers in a string and print it at once
test = ""

# Build a string with consecutive numbers and print it
for i in range(1, n + 1):
    test += str(i)

# Print the resulting string
print(test)