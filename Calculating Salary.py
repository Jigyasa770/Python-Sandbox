work_hours = [int(x) for x in input('Enter hours per day in entire week separated by space: ').split()]
wage = int(input('Enter hourly wages: '))
total = sum(work_hours)
salary = total * wage
print('Salary is ', salary)