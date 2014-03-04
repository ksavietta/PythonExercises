balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

monthlyInterestRate = 0
minimumMonthlyPayment = 0
monthlyUnpaidPayment = 0
updatedBalanceEachMonth = balance
total = 0

for month in range(1,13):
    balance = updatedBalanceEachMonth
    monthlyInterestRate = annualInterestRate/12.0
    minimumMonthlyPayment = monthlyPaymentRate*balance
    monthlyUnpaidPayment = balance - minimumMonthlyPayment
    updatedBalanceEachMonth = monthlyUnpaidPayment + (monthlyInterestRate*monthlyUnpaidPayment)
    total += minimumMonthlyPayment
    
    print "Month: " + str(month)
    print "Minimum monthly payment: " + str(round(monthlyPaymentRate*balance, 2))
    print "Remaining balance: " + str(round(updatedBalanceEachMonth, 2))

print "Total paid: " + str(round(total, 2))
print "Remaining balance: " + str(round(updatedBalanceEachMonth, 2))
