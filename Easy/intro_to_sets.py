'''
Task: Introduction to Sets

'''

def average(array):
    # your code goes here
    array = set(array)
    average = sum(array) / len(array)
    return average

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)