'''
A counter is a container that store elements as dictionary keys, and their counts are stored as dictionary values. 
Counts are allowed to be any integer value including zero or negative counts. 
The Counter class is similar to bags or multisets in other languages.

Task: Raghu is a shoe shop owner. His shop has X number of shoes. 
He has a list containing the size of each shoe he has in his shop. 
There are N number of customers who are willing to pay x_i amount of money only if they get the shoe of their desired size.
Your task is to compute how much money Raghu earned.
Input Format:
The first line contains X, the number of shoes.
The second line contains the space separated list of all the shoe sizes in the shop.
The third line contains N, the number of customers.
The next N lines contain the space separated values of the shoe size desired by the customer and x_i, the price of the shoe.

'''


from collections import Counter
shoes = int(input())
sizes = Counter(map(int, input().split()))
customers = int(input())
earnings = 0
for _ in range(customers):
    size, price = map(int, input().split())
    if sizes[size] > 0:
        earnings += price
        sizes[size] -= 1
print(earnings)
