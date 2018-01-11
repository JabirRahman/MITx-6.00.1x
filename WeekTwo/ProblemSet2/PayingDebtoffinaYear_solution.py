#!/bin/bsh/
# Note/ use test cases to have an idea about  the solution of the problem

# Paste your code into this box
# This script will calculate the remaining balance after one year
# using compound interest calculation method
# balance = the outstanding balance on the credit card
# annualInterestRate = annual interest rate as a decimal 
# monthlyPaymentRate = minimum monthly payment rate as a decimal
# Remaining balance = the balance that remains after paying a
# fixed amount of debt each month
MonthlyInterestRate = (annualInterestRate/12)
for i in range(12):
    MinimumMonthlyPayment = (monthlyPaymentRate * balance)
    MonthlyUnpaidBalance  = (balance - MinimumMonthlyPayment)
    balance = (MonthlyUnpaidBalance)+(MonthlyInterestRate * MonthlyUnpaidBalance)
Remainingbalance = round(balance,2)
print("Remaining balance:" + str(Remainingbalance))
