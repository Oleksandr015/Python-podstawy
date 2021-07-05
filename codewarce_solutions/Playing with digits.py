def dig_pow(n, p):
    sum = 0
    for i in str(n):
        sum += int(i) ** p
        p += 1
    k = sum // n
    if k != 0:
        return k
    else:
        return -1


if __name__ == '__main__':
    print(dig_pow(89, 1))  # 1
    print(dig_pow(92, 1))  # -1
    print(dig_pow(3263, 3))  # 51
