import math
import os
import random
import re
import sys


def solve(s):
    s = " ".join(word.capitalize() for word in s.split(" "))
    return s

if __name__ == '__main__':
    fptr = open(os.environ.get('OUTPUT_PATH', '/dev/stdout'), 'w')
    s = input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()