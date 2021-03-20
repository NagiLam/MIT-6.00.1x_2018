
""" Probem Set 1 - Problem 2

Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2"""

# s = 'azcbobobegghakl'

count = 0
n = 0
m = 3
temp = 0
length = len(s)
while (temp < length - 2):
    if (s[n:m] == 'bob'):
        count = count + 1
    temp += 1
    n += 1
    m += 1
print("Number of times bob occurs is: " + str(count))
