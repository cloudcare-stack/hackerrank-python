'''
Task: Find the number of occurrences of a substring in a given string.
'''

def count_substring(string, sub_string):
    # count the number of occurrences of sub_string in string
    count = 0
    print(len(string), len(sub_string))
    # loop through the string and check for occurrences of sub_string
    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i+len(sub_string)] == sub_string:
            count += 1
    return count

if __name__ == '__main__':
    # read the string and the substring to count
    string = input().strip()
    sub_string = input().strip()
    # count the occurrences of sub_string in string
    count = count_substring(string, sub_string)
    print(count)