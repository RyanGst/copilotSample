#  Read 5 ages and average the ages (use a variable for age)

# read the ages
ages = []
for i in range(0, 5):
    age = int(input())
    ages.append(age)

# calculate the average
average_age = sum(ages) / len(ages)

# print the average
print('Average age: {:.2f}'.format(average_age))
