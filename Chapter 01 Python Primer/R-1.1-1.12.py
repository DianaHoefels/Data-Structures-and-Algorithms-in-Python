# R-1.1 Write a short Python function, is multiple(n, m),
# that takes two integer values and returns True if n
# is a multiple of m, that is, n = mi for some integer i,
# and False otherwise.

def multiple(n, m):
    return False

# Write a short Python function is_even(k), that takes an integer value and returns True
# if k is even, and False otherwise. However, your function cannot use the multiplication, modulo,
# or division operators.

def is_even(int_value):
    is_even = True
    for i in range(1, int_value + 1):
        if is_even == True:
            is_even = False
        else:
            is_even = True

    return is_even

print(is_even(1))

# R-1.3 Write a short Python function, minmax(data), that takes a sequence of one or more numbers,
# and returns the smallest and largest numbers, in the form of a tuple of length two.
# Do not use the built-in functions min or max in implementing your solution.

def minmax(data):
    sortedlist = sorted(data)

    return (sortedlist[0], sortedlist[-1])

# R-1.8 Python allows negative integers to be used as indices into a sequence,
# such as a string. If string s has length n, and expression s[k] is used for index −n ≤ k < 0,
# what is the equivalent index j ≥ 0 such that s[j] references the same element?


# R-1.9 What parameters should be sent to the range constructor,
# to produce a range with values 50, 60, 70, 80?

for i in range(50, 90, 10):
    pass#print(i)

# R-1.10 What parameters should be sent to the range constructor,
# to produce a range with values 8, 6, 4, 2, 0, −2, −4, −6, −8?

for i in range(8, -10, -2):
    pass #print(i)

#R-1.11 Demonstrate how to use Python’s list comprehension syntax to produce the
# list [1, 2, 4, 8, 16, 32, 64, 128, 256].

n = 9
mylist = [1 << i for i in range(n)]
print(mylist)

# R-1.12 Python’s random module includes a function choice(data) that returns a random
# element from a non-empty sequence. The random module includes a more basic function randrange,
# with parameterization similar to the built-in range function,
# that return a random choice from the given range. Using only the randrange function,
# implement your own version of the choice function.
