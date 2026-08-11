'''
Task: Identify the presence of alphanumeric characters, 
alphabetical characters, digits, lowercase and uppercase characters in a given string.
'''

if __name__ == '__main__':
    # read the string
    s = input()
    # check for alphanumeric characters
    print(any(c.isalnum() for c in s))
    # check for alphabetical characters
    print(any(c.isalpha() for c in s))
    # check for digits
    print(any(c.isdigit() for c in s))
    # check for lowercase characters
    print(any(c.islower() for c in s))
    # check for uppercase characters
    print(any(c.isupper() for c in s))