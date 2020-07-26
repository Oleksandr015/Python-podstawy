from abc import ABC, abstractmethod
from typing import List


class Task:
    def __init__(self, description: str, points: int):
        self.description: str = description
        self.points: int = points
        self.is_done: bool = False

    def execute(self):
        self.is_done = True

    def __repr__(self):
        return f'Task({self.description},{self.points})'


class Employee(ABC):
    def __init__(self, name: str, age: int):
        self.name: str = name
        self.age: int = age
        self.list_tasks: List[Task] = []

    def about(self):
        return f'Hello, my name is {self.name}, I am {self.age} old.'  # opis (zwraca przedstawienie się (imię i wiek))

    def work(self):
        for task in self.list_tasks:
            if not task.is_done:
                task.execute()

    def add_task(self, task: Task):
        self.list_tasks.append(task)

    @property
    def points(self) -> int:
        return sum([task.points for task in self.list_tasks if task.is_done])

    @property
    def description(self) -> str:
        return f'{self.name},{self.age} years old'


class SalariedEmployee(Employee):
    def __init__(self, name: str, age: int, weekly_salary: float):
        super().__init__(name, age)
        self.weekly_salary: float = weekly_salary

    @property
    def monthly_salary(self) -> float:
        return 4 * self.weekly_salary

    @property
    def description(self) -> str:
        return f'{super().description}, I earn {self.monthly_salary}'


class HourlyEmployee(Employee):
    def __init__(self, name: str, age: int, salary_per_hour: float, count_hours: int):
        super().__init__(name, age)
        self.salary_per_hour: float = salary_per_hour
        self.count_hours: int = count_hours

    @property
    def monthly_salary(self) -> float:
        return self.salary_per_hour * self.count_hours * 4

    @property
    def description(self) -> str:
        return f'{super().description}, I work {self.count_hours} hours weekly, {self.salary_per_hour}'


class Company():
    def __init__(self, name: str):
        self.name: str = name
        self.employees: List[Employee] = []
        self.tasks: List[Task] = []

    def hire_employee(self, employee: Employee):
        self.employees.append(employee)

    def hire_employees(self, employees: List[Employee]):
        for employee in employees:
            self.hire_employee(employee)

    def add_task(self, task: Task):
        self.tasks.append(task)

    def add_tasks(self, tasks: List[Task]):
        for task in tasks:
            self.add_task(task)

    def welcome_employees(self):
        return '\n'.join([employee.description for employee in self.employees])

    @property
    def count_employees(self):
        list_employees = self.employees
        return len(list_employees)




if __name__ == '__main__':
    employee1 = Employee('Anna', 18)
    task = [Task('Buy bananas', 3), Task('Clean Room', 5), Task('Sell Mac', 10)]
    print(task[0])
    task[0].execute()
    print(task[0].is_done)
    print(task[0].execute())

    employee_1 = SalariedEmployee('Piotr', 25, 1000)
    employee_2 = HourlyEmployee('James', 23, 20, 2000)
    print(employee_1.description)
    print(employee_2.description)
    employee_1.add_task(Task('Buy 2563', 5))
    print(employee_1.list_tasks)
    print(employee_1.points)
    employee_1.work()
    print(employee_1.points)
    print()
    employee_1 = SalariedEmployee('Piotr', 25, 1000)
    employee_2 = HourlyEmployee('James', 23, 20, 2000)
    employee_3 = HourlyEmployee('Ewa', 20, 27, 2700)
    print(employee_1.monthly_salary)
    print(employee_2.monthly_salary)
    print(employee_3.monthly_salary)
    print()
    print(employee_1.description)
    print(employee_2.description)
    print(employee_3.description)
    print()


    company1 = Company('Apple')
    tasks = [Task('Buy ananas', 8), Task('Clean Room', 475), Task('Sell Mac', 108), Task('Buy bananas', 358),
             Task('Clean Room', 7)]
    company1.add_tasks(tasks)
    print(company1.tasks)
    employees = [Employee('Anna', 18),
                 SalariedEmployee('Piotr', 25, 1000),
                 HourlyEmployee('James', 23, 20, 2000),
                 HourlyEmployee('Ewa', 20, 27, 2700)]

    company1.hire_employees(employees)
    print((company1.employees))
    print(company1.count_employees)
