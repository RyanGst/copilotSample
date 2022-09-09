#  Make an algorithm that takes the base salary of an employee, calculates and writes the amount of the increase, the new salary and the percentage of the increase
base_salary = float(input("Enter the base salary: "))
percentage_increase = float(input("Enter the percentage of the increase: "))
increase = base_salary * (percentage_increase / 100)
new_salary = base_salary + increase
print("The amount of the increase is", increase, "the new salary is", new_salary, "and the percentage of the increase is", percentage_increase)
