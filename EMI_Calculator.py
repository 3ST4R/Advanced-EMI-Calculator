# -*- coding: utf-8 -*-
from calendar import mdays
from datetime import date, timedelta
import os
print("="*95)
print("\t\t\t\t\tEMI Calculator")
print("="*95)
print()
rupee = chr(8377)
loan_amt = int(input(" Loan Amount: {}".format(rupee)))
print()
interest = float(input(" Interest rate(in %): "))
print()
interest = interest/(12 * 100)
tenure = float(input(" Tenure(in years): "))
print()
tenure = tenure * 12

emi = (loan_amt * interest * pow(1 + interest, tenure))/(pow(1 + interest, tenure) - 1)
print('\n')
print(" Monthly EMI: {}{:.2f}".format(rupee, emi))
print('\n')
print(' EMI Date\t\tPrincipal\t\t  Interest\t\t    EMI\t\t\t  Balance')
print('-'*115)
today = date.today()
i = 1
I = []; P = []; E = []
while i <= tenure:
    if today.year % 4 != 0:
        next_month_of_today = today + timedelta(mdays[today.month])
        interest_amt = interest * loan_amt
        I.append(interest_amt)
        principal = emi - interest_amt
        P.append(principal)
        E.append(emi)
        balance = loan_amt - principal
        print(next_month_of_today.strftime(' %Y %B\t%d'), '{:>10}'.format(rupee + '{:>.2f}'.format(abs(principal))) + '\t\t' + '{:>10}'.format(rupee + '{:>.2f}'.format(abs(interest_amt))) + '\t\t' + '{:>10}'.format(rupee + '{:>.2f}'.format(abs(emi))) + '\t\t' + '{:>10}'.format(rupee + '{:>.2f}'.format(abs(balance))), sep='     ')
        today = next_month_of_today
        loan_amt = loan_amt - principal
    elif today.year % 4 == 0:
        mdays[2] = 29
        next_month_of_today = today + timedelta(mdays[today.month])
        interest_amt = interest * loan_amt
        I.append(interest_amt)
        principal = emi - interest_amt
        balance = loan_amt - principal
        P.append(principal)
        E.append(emi)
        print(next_month_of_today.strftime(' %Y %B\t%d'), '{:>10}'.format(rupee + '{:>.2f}'.format(abs(principal))) + '\t\t' + '{:>10}'.format(rupee + '{:>.2f}'.format(abs(interest_amt))) + '\t\t' + '{:>10}'.format(rupee + '{:>.2f}'.format(abs(emi))) + '\t\t' + '{:>10}'.format(rupee + '{:>.2f}'.format(abs(balance))), sep='     ')
        today = next_month_of_today
        loan_amt = loan_amt - principal
        mdays[2] = 28
    i+=1
print('\n')
interest_percent = sum(I)/sum(E)
principal_percent = sum(P)/sum(E)
print(" Total Amount to be paid: {}{:.2f}".format(rupee, sum(E)))
print()
print(" Total Interest to be paid: {}{:.2f}".format(rupee, sum(I)))
print()
print(" Principal Percentage: {:.2%}".format(principal_percent), "Interest Percentage: {:.2%}".format(interest_percent), sep='\t\t\t\t\t')
print()
print('\n')
os.system("PAUSE")

    
