from abc import  ABC
from typing import List


class Task:
    def __init__(self, task: str, points: int):
        self.task: str = task
        self.points: int = points
        self.is_end: bool = False

    def execute(self):
        self.is_end = True

    def __repr__(self) -> str:
        return f'Employee({self.task}, {self.points})'


class Employee(ABC):
    def __init__(self, name: str, age: int):
        self.name: str = name
        self.age: int = age
        self.list_tasks: List[Employee] = []

    def description(self) -> str:
        return f'My name is {self.name}, i am {self.age} years old!'


    def __repr__(self) -> str:
        return f'Employee({self.name}, {self.age})'


    def add_task(self, task: Task):
        self.list_tasks.append(task)

    def working(self):
        for task in self.list_tasks:
            if self.is_end:
                self.list_tasks.append(task)
                if self.list_tasks:
                    self.list_tasks[0].execute()

    #@property
    #def sum_points(self):
    #    points = []
    #    for task in self.list_tasks:
    #        if not task.is_end:
    #          points.append(task[1])
    #    return sum(points)

    @property
    def points(self) -> int:

        return sum([task.points for task in self.list_tasks if task.is_end])



class SalariedEmployee(Employee):
    def __init__(self, name: str, age: int, salary_per_week: float):
        super().__init__(name, age)
        self.salary_per_week: float = salary_per_week

    def weekly_salary(self) -> float:
        return self.salary_per_week  * 4

    @property
    def description(self) -> str:
        return f'{super().description()}, I earn {self.weekly_salary()}'


class HourlyEmployee(Employee):
    def __init__(self, name: str, age: int, salary_per_hour: float, hours_in_week: int):
        super().__init__(name, age)
        self.salary_per_hour: float = salary_per_hour
        self.hours_in_week: int = hours_in_week

    def hourly_salary(self) -> float:
        return self.salary_per_hour  * self.hours_in_week * 4

    @property
    def description(self) -> str:
        return f'{super().description()}, I earn  {self.hourly_salary()}'


class Company:
    def __init__(self, name: str):
        self.name: str = name
        self.list_employees: List[Employee] = []
        self.list_tasks: List[Task] = []

    def add_employee(self, employee: Employee):
        self.list_employees.append(employee)


    def add_employees(self, employee: Employee):
        for employee in self.list_employees:
            self.add_employee(employee)

    def add_task(self, task: Task):
        self.list_tasks.append(task)

    def add_tasks(self, task: Task):
        for task in self.list_tasks:
            self.list_tasks.append(task)

    def sort_task(self, list_tasks: List[Task], list_employees: List[Employee]):
        for index, task in enumerate(list_tasks):
            list_tasks[index % len(list_employees)].add_tasks(task)

    @property
    def salary_for_all(self):
        return sum([employee.monthly_salary for employee in self.employees])

    @property
    def size(self):
        return len([self.list_employees])

    @property
    def welcome_employees(self):
        return f'Welcome {self.name}'






if __name__ == '__main__':
    task_1 = Task('Buy some eats', 10)
    task_2 = Task('Clean Room', 5)
    task_3 = Task('Sell Macbook', 10)
    print(task_1)
    employee_1 = Employee('John', 25)
    print(employee_1.list_tasks)
    employee_1.add_task(task_1)
    employee_1.add_task(task_2)
    employee_1.add_task(task_3)

    employee_1 = SalariedEmployee('Piotr', 25, 1000)
    employee_2 = HourlyEmployee('James', 23, 20, 2000)
    print(employee_1.description)
    print(employee_2.description)
    employee_1.add_task(Task('Buy 2563', 5))
    # print(employee_1.tasks)
    print(employee_1.points)
    employee_1.work()
    print(employee_1.points)
    print()
    employee_1 = SalariedEmployee('Piotr', 25, 1000)
    employee_2 = HourlyEmployee('James', 23, 20, 2000)
    employee_3 = HourlyEmployee('Ewa', 20, 27, 2700)

    tasks = [Task('Buy ananas', 8), Task('Clean Room', 475), Task('Sell Mac', 108), ('Buy bananas', 358),
             Task('Clean Room', 7)]
    company = Company('Apple')
    company.add_tasks()

    print(company.welcome_employees())

    company.count_employees()
    print(company.count_employees())
