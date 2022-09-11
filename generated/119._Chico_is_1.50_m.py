#  Chico is 150m tall and grows 2 centimeters a year, while Juca is 110 m tall and grows 3 centimeters a year Build an algorithm that calculates and prints how many years it will take for Juca to be higher than Chico


# read the initial heights
chico_height = 150
juca_height = 110

# read the growth rate
chico_growth = 2
juca_growth = 3

# calculate the years
years = 0
while chico_height >= juca_height:
    chico_height += chico_growth
    juca_height += juca_growth
    years += 1

# print the result
print('Years: {}'.format(years))