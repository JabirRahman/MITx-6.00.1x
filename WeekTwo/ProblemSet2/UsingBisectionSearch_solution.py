#!/bin/bsh/
# Paste your code into this box
monthlyinterestrate = (annualInterestRate/12.0)

min_monthlypay = (balance/12)
incr_balance = (((1 + monthlyinterestrate)**12) * balance )

max_monthlypay = (((1 + monthlyinterestrate)**12) * balance )/12.0

Monthlypaidbalance = 0
Totalpaid = 0
epsilon = 0.03
difference = balance
while abs(difference) > epsilon:
    Monthlypaidbalance = (max_monthlypay + min_monthlypay)/2
    difference = balance

    for i in range(12):  
        difference = (difference - Monthlypaidbalance) + ((difference - Monthlypaidbalance) * monthlyinterestrate)

    if (difference < (-epsilon)):
        max_monthlypay = Monthlypaidbalance
            
    elif (difference > (epsilon)):
        min_monthlypay = Monthlypaidbalance
    else:
        break
Monthlypaidbalance = round(Monthlypaidbalance, 2)
print("Lowest Payment:" + str (Monthlypaidbalance))
