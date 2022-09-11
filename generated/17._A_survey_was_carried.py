#  A survey was carried out among the inhabitants of a region Data on age, sex (M/F) and salary were collected and informs:
#  a) the average salary of the group; b) number of women earning up to R$150000

survey_results = []

for i in range(0, 5):
    [s, salary] = input().split(' ')[:2]
    survey_results.append((s, float(salary)))

# find the average value in a array of tuples

average_salary = sum([x[1] for x in survey_results]) / len(survey_results)

print('Average salary: R$ {:.2f}'.format(average_salary))

# count number of values in a array of tuples that match a condition (salary <= 150000)
# and are of a specific type (F)

number_of_womans = len([x for x in survey_results if x[0] == 'F' and x[1] >= 150000])

print('Number of womans earning more than 150000: {}'.format(number_of_womans))