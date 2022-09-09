# Write a python program to read an integer and tell if it is divisible by 5
# 
#  Example:
#  Number: 15
#  It is divisible by 5 ]

# Solution
# Read an integer
number = int(input('Number: '))

# Tell if it is divisible by 5
if number % 5 == 0:
    print('It is divisible by 5')
else:
    print('It is not divisible by 5')