#  Read an integer value (only accept values ​​between 1 and 10) and write the multiplication table from 1 to 10 of the read value

# read the number
number = int(input())


if number < 1 or number > 10:
    print('Invalid number')
    exit()

# print the multiplication table
for i in range(1, 11):
    print('{} x {} = {}'.format(number, i, number * i))
