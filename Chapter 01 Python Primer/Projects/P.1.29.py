# Write a Python program that outputs all possible strings formed by using the characters
# 'c','a', 't', 'd', 'o' and 'g' exactly once.
import itertools

# recursively

def permutate_1(start, characters=''):
    if len(start) == 0:
        print(characters)
    else:
        for i in range(len(start)):
            permutate_1(start[:i] + start[i+1:], characters + start[i])

# or with the built-in permutation function from itertools library.

def permutate_2(characters):

    all_strings = list(itertools.permutations(characters))

    return ["".join(character) for character in all_strings]


if __name__ == '__main__':
    sequence_characters = ['c','a', 't', 'd', 'o', 'g']
    print(permutate_1(sequence_characters))
    print(permutate_2(sequence_characters))
