class Employee:
    employee_count = 101
    def __init__(self, name, salary, designation):
        self.name = name
        self.salary = salary
        self.designation = designation
        self.eid = 'e' + str(Employee.employee_count)
        Employee.employee_count += 1
    def show_details(self):
        print(self.name)
        print(self.eid)
        print(self.designation)
        print(self.salary)
    @classmethod
    def total_emp(cls):
        return cls.employee_count - 101

e1 = Employee('John', 30000, 'Worker')
e2 = Employee('Mark', 100000, 'Manager')
e1.show_details()
print(" ")
e2.show_details()
print(" ")
print(e1.total_emp())