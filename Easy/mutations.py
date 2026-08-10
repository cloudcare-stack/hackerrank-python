'''
Task: Read a string and change the character at a given index and print the modified string.

Understand immutable vs mutable by making changes to a given string.
'''

def mutate_string(string, position, character):
    # convert string to list to make it mutable
    string_list = list(string)
    # change the character at the given position
    string_list[position] = character
    # convert list back to string
    return ''.join(string_list)

if __name__ == '__main__':
    # read the string and the position and character to change
    s = input()
    # read the position and character to change
    i, c = input().split()
    # convert position to integer
    s_new = mutate_string(s, int(i), c)
    print(s_new)