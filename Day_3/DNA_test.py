def check_dna_distance_two(parent_dna, child_dna):
    distance = 0
    for i in in parent_dna:
        if parent_dna[index] != child_dna[index]:
            distance += 1
        else:
            continue
    return distance



def check_dna_distance(parent_dna, child_dna):
    distance = 0
    for index in range(len(parent_dna)):
        if parent_dna[index] != child_dna[index]:
            distance += 1
        else:
            continue
    return distance


if __name__ == '__main__':
    parent_dna = 'ACTGCTGA'
    child_dna = 'ACTGTTGA'
    print(check_dna_distance(parent_dna, child_dna))
