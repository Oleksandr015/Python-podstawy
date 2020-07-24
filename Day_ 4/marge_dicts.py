def merge_dicts(first_dict, second_dict):
    merged_dict = {}
    print(first_dict.items())
    for key, value in first_dict.items():
        merged_dict[key] = value

    for key, value in second_dict.items():
        if key in merged_dict:
            merged_dict[key] += second_dict[key]
        else:
            merged_dict[key] = second_dict[key]

    return merged_dict


def marge_dict_info_tuples(first_dict, second_dict):
    merged_dict = {}
    for key, value in first_dict.items():
        merged_dict[key] = value

    for key, value in second_dict.items():
        if key in merged_dict:
            merged_dict[key] = (merged_dict[key], value)
        else:
            merged_dict[key] = value

    return merged_dict





if __name__ == '__main__':
    first_dict = {'a': 4, 'b': 7, 'c': 1}
    second_dict = {'a': 2, 'c': 8, 'z': 11}
    result_dict = merge_dicts(first_dict, second_dict)
    print(result_dict)
    """
    {'a': 6, 
     'b': 7, 
     'c': 9, 
     'z': 11}
    """

    print(marge_dict_info_tuples(first_dict, second_dict))
