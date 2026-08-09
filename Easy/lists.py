'''
Task: Create a list and perform various operations on it.
'''

N = int(input())

integer_list = []
for _ in range(N):

    command = input().split()

    if command[0] == 'insert':
        integer_list.insert(int(command[1]), int(command[2]))
    elif command[0] == 'print':
        print(integer_list)
    elif command[0] == 'remove':
        integer_list.remove(int(command[1]))
    elif command[0] == 'append':
        integer_list.append(int(command[1]))
    elif command[0] == 'sort':
        integer_list.sort()
    elif command[0] == 'pop':
        integer_list.pop()
    elif command[0] == 'reverse':
        integer_list.reverse()
