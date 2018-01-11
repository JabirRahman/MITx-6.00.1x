#!/bin/bsh/

def isIn(char, aStr):
    if (len(aStr) == 0):
        return False
    elif (len(aStr) == 1):
        if (char == aStr[0]):
            return True
        else:
            return False
        
    elif (len(aStr) % 2 == 0):
        mid = int(len(aStr)/2)
    else:
        mid = (int(len(aStr)/2) + 1)
        
    mid_char = aStr[mid]    
    if (char == mid_char):
        return True
    else:
        if (char < mid_char):
            aStr = aStr[0:mid]
            return isIn(char, aStr)
        else:
            aStr = aStr[-mid:]
            return isIn(char, aStr)
