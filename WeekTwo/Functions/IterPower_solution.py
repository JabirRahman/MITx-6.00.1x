#!/bin/bsh/
def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    i_num = 1
    for i in range(exp):
        i_num = i_num * base
    return (i_num)
