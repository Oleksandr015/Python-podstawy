def max_sequence(numbers):

    best_sum = 0  # or: float('-inf')
    current_sum = 0
    for x in numbers:
        current_sum = max(0, current_sum + x)
        best_sum = max(best_sum, current_sum)
    return best_sum

if __name__ == '__main__':
    print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))