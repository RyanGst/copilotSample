#  Make a program to receive an integer number from the user and determine if this number is prime or not Prime
#

# read a number
number = int(input('Type a number: '))

# write a function to check if the number is prime
def is_prime(number):
    if number == 1:
        return False
    elif number == 2:
        return True
    else:
        for i in range(2, number):
            if number % i == 0:
                return False
        return True


# print the result
if is_prime(number):
    print('The number is prime')
else:
    print('The number is not prime')