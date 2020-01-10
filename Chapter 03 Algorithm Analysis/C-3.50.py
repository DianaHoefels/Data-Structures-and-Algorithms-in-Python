# (a) Describe a simple O(n2)-time algorithm for computing p(x).

def polynomial_one(x, n, coefficient_list):
    """O^2 method for computing p(x).
    
    Parameters
    ----------
    x : number
        The value for x.
    n : int
        The degree of the polynomial.
    coefficient_list: list
        The list of coefficients of the polynomial, from the highest to the lowest degree.
    Returns
    -------
    p_x : number
        The result of the polynomial evaluated for the given x, n and coefficients.
    RUNTIME
    --------
    0(n^2)
    """
    p_x = 0

    for idx, coef in enumerate(reversed(coefficient_list)):
        exp = 1
        for _ in range(idx):
            exp *= x
        p_x += coef * exp

    return p_x
# (b) Describe an O(n log n)-time algorithm for computing p(x), based upon i
# a more efficient calculation of x .

def power(x, n):
    """
    Helper method to compute x to the power of n
    Parameters
    ----------
    x : number
        The value for x, the base.
    n : number
        The value for n, the exponent.
    Returns
    -------
    x ** n
    """
    if n == 0: 
        return 1
    if n % 2 == 0: # if n even
        partial = power(x, n // 2)
        return partial * partial
    else:

      return x * power(x, n -1) # if n odd

# (c) Horner’s method. 

def polynomial_two(x, n, coefficient_list):
    """O(n log n) method for computing p(x), using power_two(x, n) to compute the n-th power of x in O(log n) time.
    
    Parameters
    ----------
    x : number
        The value for x.
    n : int
        The degree of the polynomial.
    coefficient_list: list
        The list of coefficients of the polynomial, from the highest to the lowest degree.
    Returns
    -------
    p_x : number
        The result of the polynomial evaluated for the given x, n and coefficients.
    Runtime
    --------
    O(n log n)
    """
    p_x = 0

    for idx, coef in enumerate(reversed(coefficient_list)):
        p_x += coef * power(x, idx)
    return p_x

def polynomial_three(x, n, coefficient_list):
    """
    Horner's method to compute p(x).
    Parameters
    ----------
    x : number
        The value for x.
    n : int
        The degree of the polynomial.
    coefficient_list: list
        The list of coefficients of the polynomial, from the highest to the lowest degree.
    Returns
    -------
    p_x : number
        The result of the polynomial evaluated for the given x, n and coefficients.
    Time Complexity: O(n)
    Number of Multiplications: O(n)
    Number of Additions: 0(n)
    """
    p_x = 0
    for i in coefficient_list:
         p_x *= x + i

    return p_x