def count_present(first_list):
    count = 0
    for student in first_list:
        if student:
            count += 1
    return count


def absent_ratio(first_list):
    count = 0
    for student in first_list:
        if student == False:
            count += 1
    return count


def perfect_student_indexes(first_list, second_list):
    count = []
    for student in range(len(first_list)):
        if first_list[student] == second_list[student] == True:
            count.append(student)
    return count


def lazy_students_indexes(first_list, second_list):
    count = 0
    for student in range(len(first_list)):
        if first_list[student] == False or second_list[student] == False:
            count += 1
    return count


def parse_attendance_string(attendance_string_two):
    attendance_string_list = []
    for i in attendance_string_two:
        if i == 'T':
            attendance_string_list.append(True)
        else:
            attendance_string_list.append(False)
    return attendance_string_list


def present_first_day(attendance_string_list):
    count = 0
    for index in attendance_string_list:
        if index == True:
            count += 1

    return count


def procent_attendance(attendance_string_list):
    return present_first_day(attendance_string_list) / len(attendance_string_list)


def perfect_student_indexes_two(attendance_str_two, attendance_str_three):
    count = []
    for student in range(len(attendance_str_two)):
        if attendance_str_two[student] == attendance_str_three[student] == True:
            count.append(student)
    return count


def parse_attendance_string(attendance_string):
    return [attendance.upper() == 'T' for attendance in attendance_string]


if __name__ == '__main__':
    first_list = [True, True, False, True, False]
    second_list = [True, True, False, False, False]
    attendance_string = 'TFTTF'
    attendance_str_two = [True, True, False, False, True, False, True, False, True, False, True]
    attendance_str_three = [True, True, False, False, True, False, True, True, False, True, False]
    attendance_string_two = "TTFFTFTFTFT"
    attendance_string_three = 'TTFFTFTTFTF'
    attendance_string_list = [True, True, False, False, True, False, True, True, False, True, False]

    print(count_present(first_list))
    print(absent_ratio(first_list))
    print(perfect_student_indexes(first_list, second_list))
    print(lazy_students_indexes(first_list, second_list))
    print(parse_attendance_string(attendance_string))
    print(parse_attendance_string(attendance_string_two))
    print(parse_attendance_string(attendance_string_three))
    print(present_first_day(attendance_string_list))
    print(procent_attendance(attendance_string_list))
    print(perfect_student_indexes_two(attendance_str_two, attendance_str_three))
    print()
    print(parse_attendance_string(attendance_string))


