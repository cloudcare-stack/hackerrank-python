'''
Task: In a classroom of N students, find the student with the second lowest grade.

Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
'''


students = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name, score])


print(students)

scores = sorted((set(score for name, score in students)))

print(scores)

second = scores[1]

print(second)

# Explaining the list comprehension used in the final print statement:
# 1. The expression (name for name, score in students if score == second)
#    creates a generator that yields the names of students whose score matches the second lowest score.
# 2. The sorted() function takes this generator and returns a sorted list of names.
for name in sorted(name for name, score in students if score == second):
    print(name)