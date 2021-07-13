import itertools


def anagrams(word, words):
    anagrams_list = ["".join(perm) for perm in itertools.permutations(word)]

    return [res for res in words if res in anagrams_list]


if __name__ == '__main__':
    print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
