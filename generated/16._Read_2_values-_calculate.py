# Read 2 values, calculate and write the sum of the integers between the 2 values ​​read (including the values ​​read in the sum)
# Consider that the second value read will always be greater than the first value

# read the first value
first_value = int(input('Type the first value: '))
# read the second value
second_value = int(input('Type the second value: '))
# initialize the sum variable
sum = 0
# iterate over the range of values ​​between the first and second values
for i in range(first_value, second_value + 1):
    # sum the values ​​in the variable
    sum += i
# print the result
print(f'The sum of the values ​​between {first_value} and {second_value} is {sum}')