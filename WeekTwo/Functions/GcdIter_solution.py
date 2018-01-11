#!/bin/bsh/
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    number = 1
    min_val = min(a,b)
    for i in range (min_val, number, -1):
        if (a% i == 0 and b%i == 0):
            number = i
            break
        else:
            number = 1
    return number
