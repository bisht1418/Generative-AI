# Problem 8: Initialize dictionary with default values
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

employee_data = {}

for employee in employees:
    employee_data[employee] = {"designation": 'Developer', "salary": 8000}
print(employee_data)
