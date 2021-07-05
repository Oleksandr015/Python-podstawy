
def positive_sum(arr):
    for i in list(arr):
        if i < 0:
            arr.remove(i)
           

    return sum(arr)


if __name__ == '__main__':
    print(positive_sum([-1,-2,-3,-4,-5]))