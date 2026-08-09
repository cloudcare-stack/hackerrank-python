'''
Task: Swap the letter cases of a given string. Upper case letters should be converted to lower case and vice versa.
'''

def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)