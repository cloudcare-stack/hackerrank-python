'''
This tool computes the cartesian product of input iterables.
It is equivalent to nested for-loops in a generator expression.
For example, product (A, B) returns the same as ((x,y) for x in A for y in B).
'''



if __name__ == '__main__':
    from itertools import product
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(*product(a, b))