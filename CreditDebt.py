#Debt check

balance = float(input('Balance: '))
annInterest = float(input('ann interest rate : ')) 
MinPayment = float(input('min pay: '))
mInterest = annInterest/12
newbalance = balance
m=0
while m<12:
	interest = newbalance*mInterest
	M_interest = interest + newbalance
	minpay = MinPayment*M_interest
	newbalance = M_interest  - minpay
	m+=1
	print('Month ', m, ' Balance ', '$',round(newbalance,2) )


	
