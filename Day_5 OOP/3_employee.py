class Employee:
    raise_amount = 1.05

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def email(self):
        return f'{self.first_name}.{self.last_name}@facebook.com'

    def apply_raise(self):
        self.salary *= self.raise_amount

    @classmethod
    def set_raise_amount(cls, new_raise_amount):
        cls.raise_amount = new_raise_amount

    def __repr__(self):
        return f'Employee({self.first_name}, {self.last_name}, {self.salary}, {self.email}'

if __name__ == '__main__':
    #employee = Employee('Piotr', 'Grzybowski', 10000)
    #print(employee)
    #print(employee.fullname())
    #employee.apply_raise()
    #print(f'New Salary: {employee.salary}')
#
    #new_employee = Employee('Eva', 'Green', 10000)
    #new_employee.apply_raise()
    #print(f'New Salary: {employee.salary}')
#
    #Employee.raise_amount = 1.20
    #employee.apply_raise()
    #new_employee.apply_raise()

    employee_1 = Employee('Piotr', 'Grzybowski', 10000)
    employee_2 = Employee('Eva', 'Green', 10000)
    print(f'Emp1: {employee_1.raise_amount}, Emp2: {employee_2.raise_amount}')
    Employee.set_raise_amount(1.07)
    print(f'Emp1: {employee_1.raise_amount}, Emp2: {employee_2.raise_amount}')
    employee_1.set_raise_amount(1.1)
    print(f'Emp1: {employee_1.raise_amount}, Emp2: {employee_2.raise_amount}')

    print(employee_1.fullname)
    print(employee_1.email)