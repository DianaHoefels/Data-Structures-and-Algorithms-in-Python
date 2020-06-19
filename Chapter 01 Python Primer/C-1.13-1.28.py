# Chapter 1. Python Primer

# Creativity

# C-1.4 Write a short Python function that takes a sequence of integer values and
# determines if there is a distinct pair of numbers in the sequence whose product
# is odd.
import itertools


def check_odd_product(sequence):
    sequence_comb = list(itertools.combinations(sequence, 2))

    return [(x,y) for x,y in sequence_comb if x * y % 2 == 1]

#print(check_odd_product([1,2,3,4,5]))

# C-1.5 Write a Python function that takes a sequence of numbers and determines
# if all the numbers are different from each other (that is, they are distinct).

def is_dictinct(sequence):
    if len(sequence) == len(set(sequence)):
        return True
    else:
        return False

#print(is_dictinct([2, 7, 9, 10, 9, 20, 23]))

# C-1.6 In our implementation of the scale function (page 25), the body of the loop executes
# the command data[j] *= factor. We have discussed that numeric types are immutable, and that use of
# the *= operator in this context causes the creation of the new instance (not the mutation of an
# existing instance). How is it still possible, then, that our implementation of scale changes the actual
# parameter sent by the caller?
def scale(data, factor):
    for j in range(len(data)):
        data[j] *= factor

#print(scale([1,2,3], 2))

# Answer: In the implementation of scale, the actual parameter sent by the caller is not changed,
# what changes in the list (as lists are mutable) are the references, as they
# no longer point to the old objects but to the new immutable ones (created with *= operator).

# C-1.7 Had we implemented the scale function (page 25) as follows, does it work properly?

def scale(data, factor):
    for val in data:
        val *= factor

# Answer: No, it does not. In this implementation not all the objects of the list are referenced from
# old objects to the new. Whereas data[i] changes the reference to all the elements of the list.

# C-1.8 Demonstrate how to use Python's list comprehension syntax to produce the list
# [0, 2, 6, 12, 20, 30, 42, 56, 72, 90]

# Answer: create a generator

def gen_num():
    result = 0
    i = 0
    while True:
        yield result
        i += 1
        result += i + i

generate_number = gen_num()
lst_demo = [next(generate_number) for _ in range(10)]

#print(lst_demo)