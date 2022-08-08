# Problem 1 - Paying Debt off in a Year

# (10/10 points)
# Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the
# credit card company each month.

# The following variables contain values as described below:
# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal
# monthlyPaymentRate - minimum monthly payment rate as a decimal

# For each month, calculate statements on the monthly payment and remaining balance. At the end of 12 months, print out the remaining
# balance. Be sure to print out no more than two decimal digits of accuracy - so print

# Remaining balance: 813.41
# instead of
# Remaining balance: 813.4141998135

# So your program only prints out one thing: the remaining balance at the end of the year in the format:
# Remaining balance: 4784.0

# A summary of the required math is found below:
# Monthly interest rate= (Annual interest rate) / 12.0
# Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
# Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
# Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

balance = 5000
monthlyPaymentRate = 0.02
annualInterestRate = 0.18

for _ in range(12):
    balance = (balance - monthlyPaymentRate*balance) + (balance - (monthlyPaymentRate*balance))*annualInterestRate/12
print(round(balance,2))



# Problem 2 - Paying Debt Off in a Year

# (15/15 points)
# Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months.
# By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be
# paid each month.

# In this problem, we will not be dealing with a minimum monthly payment rate.

# The following variables contain values as described below:
# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal

# The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year, for example:
# Lowest Payment: 180

# Assume that the interest is compounded monthly according to the balance at the end of the month (after the payment for that month is
# made).
# The monthly payment must be a multiple of $10 and is the same for all months. Notice that it is possible for the balance to become
# negative using this payment scheme, which is okay. A summary of the required math is found below:
# Monthly interest rate = (Annual interest rate) / 12.0
# Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
# Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)



balance = 5000
minimum_payment = 0
annualInterestRate = 0.18

while balance > 0:
    minimum_payment += 10
    for _ in range(12):
        balance = (balance - minimum_payment) + (balance - (minimum_payment))*annualInterestRate/12
    if balance > 0:
        balance = 5000
print(round(balance,2))
print(minimum_payment)

# Problem 3 - Using Bisection Search to Make the Program Faster

# The following variables contain values as described below:
# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal

# To recap the problem:
# We are searching for the smallest monthly payment such that we can pay off the entire balance within a year.

# What is a reasonable lower bound for this payment value? $0 is the obvious anwer, but you can do better than that.
# If there was no interest, the debt can be paid off by monthly payments of one-twelfth of the original balance,
# so we must pay at least this much every month.
# One-twelfth of the original balance is a good lower bound.

# What is a good upper bound? Imagine that instead of paying monthly, we paid off the entire balance at the end of the year.
# What we ultimately pay must be greater than what we would've paid in monthly installments,
# because the interest was compounded on the balance we didn't pay off each month.
# So a good upper bound for the monthly payment would be one-twelfth of the balance,
# after having its interest compounded monthly for an entire year.

# In short:
# Monthly interest rate = (Annual interest rate) / 12.0
# Monthly payment lower bound = Balance / 12
# Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0

# Write a program that uses these bounds and bisection search to find the smallest monthly payment to the cent
# such that we can pay off the debt within a year. 

orig_balance = 5000
balance = 5000
minimum_payment = 0
annualInterestRate = 0.18
monthly_interest_rate = annualInterestRate / 12
lower_bound = balance / 12
higher_bound = (balance * (1+monthly_interest_rate)**12)/12
epsilon = 0.05

while abs(balance) > epsilon:
    minimum_payment = (lower_bound + higher_bound)/2
    balance = orig_balance
    for _ in range(12):
        balance = (balance - minimum_payment) + (balance - (minimum_payment))*annualInterestRate/12
    if balance > epsilon:
        lower_bound = minimum_payment
    elif balance < -(epsilon):
        higher_bound = minimum_payment
    else:
        break
print(minimum_payment)
        
