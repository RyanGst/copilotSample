#  Read 10 numbers and print how many are even and how many are odd

# read the 10 numbers
numbers = input().split(' ')[:10]

# convert to int
numbers = [int(x) for x in numbers]

# count the even and odd numbers
even = 0
odd = 0

for number in numbers:
    if number % 2 == 0:
        even += 1
    else:
        odd += 1

# print the results
print('Even numbers: {}'.format(even))
print('Odd numbers: {}'.format(odd))
