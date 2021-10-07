#def gcd(a, b):
    """
    a, b: two positive integers
    Returns the greatest common divisor of a and b
    """
def gcd(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return gcd(b, a % b)    
