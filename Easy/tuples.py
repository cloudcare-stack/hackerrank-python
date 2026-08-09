'''
Task: Given an integer, n, and n space-separated integers as input, create a tuple of those n integers.  
Then compute and print its hash value.
'''
n = int(input())
integer_list = map(int, input().split())

t = tuple(integer_list)
print(hash(t))



