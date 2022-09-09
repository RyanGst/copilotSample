# A store provides 10% off for employees and 5% off for VIP customers
# Make a program that calculates the total amount to be paid by a person 
# The program should read the total value of the purchase made and a code that identifies whether the buyer is a regular customer (1), employee (2) or VIP (3)

# The program should print the total amount to be paid and the discount amount

# Example:
# Total value: 100
# Customer type: 2
# Total to be paid: 90
# Discount: 10

# Total value: 100
# Customer type: 3
# Total to be paid: 95
# Discount: 5


# Solution
# The program should read the total value of the purchase made and a code that identifies whether the buyer is a regular customer (1), employee (2) or VIP (3)
total_value = float(input('Total value: '))
customer_type = int(input('Customer type: '))

# The program should print the total amount to be paid and the discount amount
if customer_type == 1:
    discount = 0
elif customer_type == 2:
    discount = 10
elif customer_type == 3:
    discount = 5
else:
    discount = 0

total_to_be_paid = total_value - (total_value * discount / 100)
print(f'Total to be paid: {total_to_be_paid:.2f}')
print(f'Discount: {discount}')
