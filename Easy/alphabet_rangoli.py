'''
You are given an integer, N.  Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian folk art based on creation of patterns.)
'''

def print_rangoli(size):
    import string
    alphabet = string.ascii_lowercase

    # Create the rangoli pattern
    lines = []
    for i in range(size):
        s = '-'.join(alphabet[size-1:i:-1] + alphabet[i:size])
        lines.append(s.center(4*size-3, '-'))

    # Print the rangoli pattern
    print('\n'.join(lines[::-1] + lines[1:]))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)