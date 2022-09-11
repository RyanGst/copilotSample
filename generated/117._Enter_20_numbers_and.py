#  Enter 20 numbers and print the sum of the positives and the total of the negatives

# read the 20 numbers
numbers = input().split(' ')[:20]

# convert to int
numbers = [int(x) for x in numbers]

# count the positive and negative numbers
positive = 0
negative = 0

for number in numbers:
    if number > 0:
        positive += number
    else:
        negative + 1


# print the results
print('Sum of the positives: {}'.format(positive))
print('Total of the negatives: {}'.format(negative))