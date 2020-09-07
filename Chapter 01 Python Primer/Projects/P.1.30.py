# Write a Python program that can take a positive integer greater than 2 as
# input and write out the number of times one must repeatedly divide this number
# by 2 before getting a value less than 2.

def divide_count(number):
    if number < 2:
        return 0
    return 1 + divide_count(number // 2)


if __name__ == '__main__':
    number = 10
    print('Number must be divided' , '{} {}'.format(divide_count(number), 'times.'))

# OUTPUT: Number must be divided 3 times.