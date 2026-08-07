'''
Task: The provided code stub reads an integer, n, from STDIN. For all non-negative integers i < n, print i^2. See the sample for details.
Input Format:
The first and only line contains the integer, n.
Constraints:
1 <= n <= 20
Output Format:
Print n lines, one corresponding to each i.
'''

n = int(input())

# Print the square of each number from 0 to n-1
for i in range(n):
    print(i ** 2)