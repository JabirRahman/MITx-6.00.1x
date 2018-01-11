#!/bin/bsh/

# The function will calculate the perimeter and the area of the polygon
# input: n = number of sides
#        s = length of each side
# output:
#        sum = sum of square of perimeter and area of the polygon
# import math
import math

# define the function
def polysum(n, s):
    ''' use regular polygon euation to calculate the                            
        area and perimeter, be aware to calculate the                           
        square of perimeter before summation                                    
    '''                                                         
    perimeter = (n*s)
    peri_sqr = (perimeter)**2
    area = (0.25* n* s**2)/math.tan(math.pi/n)
    summation = (peri_sqr + area)
    result = round (summation, 4)
    return (result)
