""" Problem Set 2 - Problem 3 - Using Bisection Search to Make the Program Faster

In short:

Monthly interest rate = (Annual interest rate) / 12.0
Monthly payment lower bound = Balance / 12
Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0

Write a program that uses these bounds and bisection search (for more info check out the Wikipedia page on bisection search) to find the smallest monthly payment to the cent (no more multiples of $10) such that we can pay off the debt within a year. 
Try it out with large inputs, and notice how fast it is (try the same large inputs in your solution to Problem 2 to compare!). 
Produce the same return value as you did in Problem 2.

"""

monthlyInterestRate = annualInterestRate / 12.0
tempBalance = balance
lowerBound = balance / 12
upperBound = (balance * ((1 + monthlyInterestRate) ** 12)) / 12.0
minPayment = 0
epsilon = 0.01

while abs(balance) >= epsilon:
    minPayment = (lowerBound + upperBound) / 2.0
    balance = tempBalance
    for i in range (12):
        balance =  balance - minPayment + ((balance - minPayment) * monthlyInterestRate)
    if (balance > epsilon):
        lowerBound = minPayment
    elif (balance < -epsilon):
        upperBound = minPayment
    else:
        break
       
print("Lowest Payment: " + str(round(minPayment, 2)))
