#Debt check
#balance
#annualInterestRate
#monthlyPaymentRate

mInterest = annualInterestRate/12
newbalance = balance
m=0
while m<12:
        interest = newbalance*mInterest
        M_interest = interest + newbalance
        minpay = monthlyPaymentRate*M_interest
        newbalance = M_interest  - minpay
        m+=1
        #print('Month ', m, ' Balance ', '$',round(newbalance,2) )
print('Remaining balance: ', round(newbalance, 2))

	
