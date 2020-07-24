def sum_values(values):
    index = 0
    while index < len(values):
        print(values[index])
        index += 1


def print_values(values):
    index = 0
    result = 0
    while index < len(values):
        result += values[index]
        index += 1
    return result

def min_value(values):
    index = 0
    result = 99999
    while index < len(values):
        if values[index] < result:
            result = values[index]
        index += 1
    return result

if __name__ == '__main__':
    #print(sum_values([4, 9, 11]))
    #print(sum_values([4, 9, 11]))
    #print([4, 9, 11])
    print(min_value([4, 9, 11]))
