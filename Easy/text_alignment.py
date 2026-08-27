'''
Task: Generate the HackerRank logo using text alignment techniques in Python.
'''
# # Enter your code here. Read input from STDIN. Print output to STDOUT
# thickness = int(input())

# c = "H"

# for i in range(thickness):
#     print((c * (2 * i + 1)).center(thickness * 3))

# for _ in range(thickness):
#     # print(("-" * thickness) + (c * thickness).ljust(thickness * 4, '-') + (c * thickness))
#     left = (c * thickness).center(thickness * 3)
#     right = (c * thickness).center(thickness * 5)
#     print(left + right)

# for _ in range(thickness - 2):
#     print((c * thickness * 5).center(thickness * 7))

# for _ in range(thickness):
#     # print(("-" * thickness) + (c * thickness).ljust(thickness * 4, '-') + (c * thickness))
#     left = (c * thickness).center(thickness * 3)
#     right = (c * thickness).center(thickness * 5)
#     print(left + right)

# for i in range(thickness - 1, -1, -1):
#     right = (c * (2 * i + 1)).center(thickness * 3)
#     left = (" " * thickness).center(thickness * 4)
#     print(left + right)

thickness = int(input())
c = "H"

# Top cone
for i in range(thickness):
    print(
        (c * i).rjust(thickness - 1)
        + c
        + (c * i).ljust(thickness - 1)
    )

# Top pillars
for i in range(thickness + 1):
    print(
        (c * thickness).center(thickness * 2)
        + (c * thickness).center(thickness * 6)
    )

# Middle belt
for i in range((thickness + 1) // 2):
    print((c * thickness * 5).center(thickness * 6))

# Bottom pillars
for i in range(thickness + 1):
    print(
        (c * thickness).center(thickness * 2)
        + (c * thickness).center(thickness * 6)
    )

# Bottom cone
for i in range(thickness):
    print(
        (
            (c * (thickness - i - 1)).rjust(thickness)
            + c
            + (c * (thickness - i - 1)).ljust(thickness)
        ).rjust(thickness * 6)
    )
