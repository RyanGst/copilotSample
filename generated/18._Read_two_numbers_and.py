#  Read two numbers and print all numbers between them Suppose the second number is greater than the first
# 

# read the two numbers
a, b = input().split(' ')[:2]

# convert to int
a = int(a)
b = int(b)

# print all numbers between a and b
for i in range(a + 1, b):
    print(i)
