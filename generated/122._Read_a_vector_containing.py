#  Read a vector containing the grades of a class of 10 students Calculate the class average and count how many students scored above this calculated average Write the class average and the counting result

# read the grades
grades = [float(x) for x in input().split(' ')[:10]]

# calculate the average
average = sum(grades) / len(grades)

# count the students above the average
count = 0

for grade in grades:
    if grade > average:
        count += 1

# print the results
print('Class average: {}'.format(average))
print('Students above the average: {}'.format(count))
