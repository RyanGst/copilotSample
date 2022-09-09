#  A company will grant a salary increase to its employees, which varies according to the position, as shown in the table below Make an algorithm that reads an employee's salary and job title (by code) and calculates the new salary If the employee's job title is not on the table, then the employee should receive a 40% raise Show the old salary, the new salary and the difference
# 
# Job code 	Job title 	Salary increase
# 1 	Manager 	10%
# 2 	Supervisor 	15%
# 3 	Officer 	20%
# 4 	Worker 	40%
# 
# 
# Example:
# Salary: 1000
# Job code: 1
# Old salary: 1000
# New salary: 1100
# Salary increase: 100
# 
# Salary: 1000
# Job code: 5
# Old salary: 1000
# New salary: 1400
# Salary increase: 400
# 
# 
# Solution
# A company will grant a salary increase to its employees, which varies according to the position, as shown in the table below Make an algorithm that reads an employee's salary and job title (by code) and calculates the new salary If the employee's job title is not on the table, then the employee should receive a 40% raise Show the old salary, the new salary and the difference
salary = float(input('Salary: '))
job_code = int(input('Job code: '))
 
# Job code 	Job title 	Salary increase
# 1 	Manager 	10%
# 2 	Supervisor 	15%
# 3 	Officer 	20%
# 4 	Worker 	40%

if job_code == 1:
    salary_increase = 10
elif job_code == 2:
    salary_increase = 15
elif job_code == 3:
    salary_increase = 20
elif job_code == 4:
    salary_increase = 40
else:
    salary_increase = 40
    