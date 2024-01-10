#Author: Minh Nguyen
#Date: 09/22/2023
#Purpose: Python program contains solution to Problem 1
#the balance and total interest earned of the account after 5% interest was compounded 2023 times

#variables
BRUTUS_INITIAL_DEPOSIT = 1
BRUTUS_INTEREST_RATE = 0.05
CURRENT_YEAR = 2023
year = 0
brutus_balance = BRUTUS_INITIAL_DEPOSIT #this equals 1 in year 0 A.D.

while year < CURRENT_YEAR: #determine Brutus's wealth in each year up until 2023 A.D.
    year = year + 1
    brutus_balance = brutus_balance * (1 + BRUTUS_INTEREST_RATE)
    brutus_interest_earned = brutus_balance - BRUTUS_INITIAL_DEPOSIT

print("At year" + " " + str(year) + ", the balance is" + " " + str(brutus_balance) + ".")
print("At year" + " " + str(year) + ", the interest earned is" + " " + str(brutus_interest_earned) + ".")
#print Brutus's balance at the end of the year 2023 and the total interest earned in 2023 years.