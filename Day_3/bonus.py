def expiranse_bonus(experience, salary):
    if experience == 0:
        bonus = salary * 0.5
    elif experience <= 5:
        bonus = salary * 1.1
    else:
        bonus = salary * 1.15

    return bonus


def salary_bonus(salary):

    if 1000 <= salary <= 2000:
        bonus = salary * 1.2
    elif 2000< salary <= 10000:
        bonus = salary * 0.8
    else:
        bonus = 0

    return bonus

def name_bonus(name):
    if len(name) > 10:
        bonus = salary * 0.2
    elif len(name) > 5:
        bonus = salary * 0.3
    else:
        bonus = 0
    return bonus


def calculate_best_bonus(name, salary, experience):
    list_bonus = []
    list_bonus.append(expiranse_bonus(experience, salary))
    list_bonus.append(salary_bonus(salary))
    list_bonus.append(name_bonus(name))
    return max(list_bonus)


def calculate_new_salary(name, salary, experience):
    return salary + calculate_best_bonus(name, salary, experience)

if __name__ == '__main__':
    name = input()
    salary = int(input())
    experience = int(input())  # w latach
    #print(expiranse_bonus(experience, salary))
    #print(salary_bonus(salary))
    #print(name_bonus(name))
    #print(calculate_best_bonus(name, salary, experience))
    print(calculate_new_salary(name, salary, experience))


'''

John
1000
4

'''
