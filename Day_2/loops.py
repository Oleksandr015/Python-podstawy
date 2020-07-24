# def spaceax(seconds):
#    while seconds >= 0:
#        print(f"Seconds: {seconds}")
#        seconds -= 1
#
#    print("end of function")

def count_to_value(value):
    i = 0
    while i <= value:
       print(i)
       i += 1

def print_even_numbers_less_than(max_value):
    value = 0
    while value <= max_value:
        if value % 2 == 0:
            print(value)
        value += 1

if __name__ == '__main__':
    # spaceax(10)
    #count_to_value(10)
    print_even_numbers_less_than(10)



