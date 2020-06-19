# Chapter 1. Python Primer

# Creativity

# C-1.4 Write a short Python function that takes a sequence of integer values and
# determines if there is a distinct pair of numbers in the sequence whose product
# is odd.
import itertools


def check_odd_product(seq):
    seq_comb = list(itertools.combinations(seq, 2))

    return [(x,y) for x,y in seq_comb if x * y % 2 == 1]

print(check_odd_product([1,2,3,4,5]))