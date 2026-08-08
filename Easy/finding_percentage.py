'''
Task: Store a list of students and marks in a dictionary, and find the average marks obtained by a student.


'''

n = int(input())
student_marks = {}

for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores

query_name = input()


# Calculate the average marks for the queried student
# the average is calculated by summing the scores and dividing by the length or number of scores
average_marks = sum(student_marks[query_name]) / len(student_marks[query_name])

# Print the average marks rounded to 2 decimal places
# f-strings are used for formatting the output, and :.2f specifies that 
# the number should be formatted to 2 decimal places
# {} is used to insert the value of average_marks into the string
print(f"{average_marks:.2f}")
