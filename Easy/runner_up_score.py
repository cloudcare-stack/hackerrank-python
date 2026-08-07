'''
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
You are given n scores. Store them in a list and find the score of the runner-up.
Input Format:
The first line contains n. The second line contains an array A[] of n integers each separated by a space.
Constraints:
2 <= n <= 10
-100 <= A[i] <= 100
Output Format:
Print the runner-up score.
'''

n = int(input())

# Read the scores as a list of integers from input
arr = map(int, input().split())

# Convert the map object to a set to remove duplicates, then convert it back to a list
unique_scores = list(set(arr))

# Sort the unique scores in descending order
unique_scores.sort(reverse=True)

# The runner-up score is the second element in the sorted list
runner_up_score = unique_scores[1]

# Print the runner-up score
print(runner_up_score)