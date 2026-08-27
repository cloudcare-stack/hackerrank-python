from collections import defaultdict

# Read input values
# map(int, input().split()) reads two integers n and m from the input, where n is the number of words in Group A and m is the number of words in Group B.
n, m = map(int, input().split())

# Create a defaultdict to store the positions of words in Group A. 
# The defaultdict is initialized with list as the default factory, 
# so that if a key is not present in the dictionary, 
# it will automatically create an empty list for that key.
positions = defaultdict(list)

# Group A
for i in range(1, n + 1):
    word = input()
    positions[word].append(i)

# Group B
for _ in range(m):
    word = input()

    if word in positions:
        print(*positions[word])
    else:
        print(-1)