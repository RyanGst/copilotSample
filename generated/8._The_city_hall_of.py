#  The city hall of Rio de Janeiro opened a line of credit for statutory employees The maximum amount of the benefit cannot exceed 30% of the gross salary Create an algorithm that allows you to enter the gross salary and the amount of the installment and inform whether or not the loan can be granted
# 
# Example:
# Gross salary: 1000
# Installment value: 300
# The loan can be granted
# 
# Gross salary: 1000
# Installment value: 400
# The loan cannot be granted
# 
# 
# Solution
# The city hall of Rio de Janeiro opened a line of credit for statutory employees The maximum amount of the benefit cannot exceed 30% of the gross salary Create an algorithm that allows you to enter the gross salary and the amount of the installment and inform whether or not the loan can be granted
gross_salary = float(input('Gross salary: '))
installment_value = float(input('Installment value: '))
 
# The maximum amount of the benefit cannot exceed 30% of the gross salary
max_amount = gross_salary * 30 / 100
 
# Create an algorithm that allows you to enter the gross salary and the amount of the installment and inform whether or not the loan can be granted
if installment_value <= max_amount:
    print('The loan can be granted')
else:
    print('The loan cannot be granted')
    