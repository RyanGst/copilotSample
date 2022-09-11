# 21 Enter a positive integer and display the factorial of this number, remembering that 0! = 1 Example: 5! = 5x4x3x2x1 = 120 Vectors

# read a number
number = int(input())

# calculate the factorial
factorial = 1
for i in range(1, number + 1):
    factorial *= i  


# print the result
print('Factorial of {}: {}'.format(number, factorial))
