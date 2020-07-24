def find_pattern(pattern, sample_list):
    for i in sample_list:
        if pattern in i:
            return True
        else:
            return False





if __name__ == '__main__':

    sample_list = ['abc', 'def']
    pattern = 'z'
    print(find_pattern(pattern,sample_list))