#  Make an algorithm that takes a person's year of birth and current year, calculates and writes the person's age
#  calculates and displays: 
# a) the current age of that person 
# b) how old will she be in 2018

year_of_birth = int(input("Enter the year of birth: "))
current_year = int(input("Enter the current year: "))
age = current_year - year_of_birth
print("The person's age is", age)