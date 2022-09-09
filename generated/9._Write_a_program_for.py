# Write a program for the user to inform the salary received and the total amount spent 
# It should be displayed on the screen “Expenses within budget” if the amount spent does not exceed the salary amount and “Budget overrun” if the amount spent exceeds the salary amount.

salary = int(input("Enter your salary: "))
expenses = int(input("Enter your expenses: "))

if expenses > salary:
    print("Budget overrun")
else:
    print("Expenses within budget")