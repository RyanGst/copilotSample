#  Create a vector with 5 integer positions and display the product of all values

# create a vector
from functools import reduce


vector = [1, 2, 3, 4, 5]

# print the product of all values
print(reduce(lambda x, y: x * y, vector))
