'''
Given an integer, n, print the following values for each integer i from 1 to n:
1. Decimal
2. Octal
3. Hexadecimal (capitalized)
4. Binary
'''

def print_formatted(number):
    width = len(f"{number:b}")
    for i in range(1, number + 1):
        print(
            str(i).rjust(width),
            f"{i:o}".rjust(width),
            f"{i:X}".rjust(width),
            f"{i:b}".rjust(width),
        )

if __name__ == '__main__':
    number = int(input())
    print_formatted(number)