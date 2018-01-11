#!/bin/bsh/
# Paste your code into this box
Monthlyinterestrate = (annualInterestRate)/12
Minimumfixedmonthlypayment = 10
init_balance = balance
while (balance > 0): 
    for i in range(12):
        Monthlyunpaidbalance = (balance) - (Minimumfixedmonthlypayment)
        balance = (Monthlyunpaidbalance) + (Monthlyinterestrate * Monthlyunpaidbalance)
    if (balance <= 0):
        print("Lowest Payment:" + str (Minimumfixedmonthlypayment))
        break
    else:
        Minimumfixedmonthlypayment+= 10
        balance = init_balance
