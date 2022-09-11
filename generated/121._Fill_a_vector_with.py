#  Fill a vector with 10 real values ​​and display all values ​​above 100


# read a vector with 10 real values
vector = [float(x) for x in input().split(' ')[:10]]

# print the values above 100
for value in vector:
    if value > 100:
        print(value)
