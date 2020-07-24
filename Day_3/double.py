def double_characters(first_list):
    second_list = []
    for char in first_list:
        if not char in second_list:
            second_list.append(char)
    return second_list

def double_characters_two(first_list):
    print(list(set(first_list)))




if __name__ == '__main__':
    first_list = [1, 2, 3, 3, 3, 4, 5]
    print(double_characters(first_list))
    print(double_characters_two(first_list))
