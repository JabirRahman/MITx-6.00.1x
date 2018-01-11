#!/bin/bsh/
# This is the solution for week one problem set one, problem one
# No need to define 's' for the problem, it will be provided by the 
# Grader
i = 0
for letter in (s):
    if (letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u'):
        i += 1
print ('Number of vowels: ' + str(i))
