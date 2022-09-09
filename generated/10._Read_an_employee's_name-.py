# Read an employee's name, salary and category,
# if the category is equal to "m" of monthly pay, grant 10% increase,
# if equal to "h" of hourly, grant 20% increase,
# if not " m” or “h”, display the message Invalid category.
# Display the employee's name and new salary.

name = input('Type your name: ')
salary = float(input('Type your salary: '))
category = input('Type your category: ')

if category == 'm':
    salary = salary * 1.1
elif category == 'h':
    salary = salary * 1.2
else:
    print('Invalid category')

    