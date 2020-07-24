def compute_bmi(weight, height):
    bmi = weight / height ** 2

    if weight <18.5:
        result = 'underweight'
    elif bmi > 25:
        result = 'overweight'
    else:
        result = 'normal'
        return result

#if __name__ == '__main__':
#   print(compute_bmi(83, 1.91))

def is_close(distance):
    if distance < 100:
        result = 'Close!'
    else:
        result = 'So far'

        return result


if __name__ == '__main__':
    print(is_close(33))


print(f"User's BMI equals to {compute_bmi(83, 1.91)}")