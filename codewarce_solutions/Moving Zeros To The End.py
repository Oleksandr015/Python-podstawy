def move_zeros(array):
    left_arr = []
    right_arr = []
    for a in array:
        if a == 0:
            right_arr.append(a)
        else:
            left_arr.append(a)
    return left_arr + right_arr

if __name__ == '__main__':
    print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9])) #[1, 2, 1, 1, 3, 1, 0, 0, 0, 0])