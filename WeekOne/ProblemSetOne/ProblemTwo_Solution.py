#!/bin/bsh/
# No need to define 's', it will be provided by the grader

i = len(s)
number = 0
for num in range (i -2):
    if s[num] == 'b' and s[(num + 1)] == 'o' and s[(num + 2)] == 'b':
        number+=1
print(number)
