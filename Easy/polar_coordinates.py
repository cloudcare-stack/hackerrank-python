'''
Polar coordinates are an alternative way of representing Cartesian coordinates or Complex Numbers.

In this problem, you are given a complex number and your task is to convert it to polar coordinates.

Python's cmath module provides a function called polar() that can be used to convert a complex number to polar coordinates. The polar() function takes a complex number as input and returns a tuple containing the magnitude (r) and the angle (theta) in radians.

'''


import cmath


c = complex(input())
r, theta = cmath.polar(c)
print(r)
print(theta)
