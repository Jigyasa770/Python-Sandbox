#USING CALLER CLASS
class Dept:
    def __init__(self):
        self.depts = {'hr': 'Human Resource Department',
                      'acc': 'Accounts and Finance Department',
                      'sd': 'Sales and Distribution Department',
                      'mkt': 'Marketing Department'}

    def __call__(self, dept):
        return self.depts[dept]

d = Dept()
s = d('hr')
print(s)

#CALLER CLASS TO CLOSURE FUNCTION
def Dept():
    depts = {'hr': 'Human Resource Department',
                      'acc': 'Accounts and Finance Department',
                      'sd': 'Sales and Distribution Department',
                      'mkt': 'Marketing Department'}

    def dname(dept):
        return depts[dept]
    return dname

d = Dept()
s = d('hr')
print(s)