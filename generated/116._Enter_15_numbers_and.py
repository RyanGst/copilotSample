#  Enter 15 numbers and print how many numbers greater than 30 have been entered

# read the 15 numbers
numbers = input().split(' ')[:15]

# convert to int
numbers = [int(x) for x in numbers]

# count the numbers greater than 30
count = 0

for number in numbers:
    if number > 30:
        count += 1

# print the result
print('Numbers greater than 30: {}'.format(count))