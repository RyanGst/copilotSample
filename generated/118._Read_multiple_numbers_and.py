#  Read multiple numbers and report how many numbers between 100 and 200 were entered When the value 0 (zero) is read, the algorithm must stop executing

# read the numbers using while loop
numbers = []
number = int(input())
while number != 0:
    numbers.append(number)
    number = int(input())

# count the numbers between 100 and 200
count = 0
for number in numbers:
    if 100 < number < 200:
        count += 1

# print the result
print('Numbers between 100 and 200: {}'.format(count))