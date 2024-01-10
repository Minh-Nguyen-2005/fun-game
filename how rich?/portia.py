#Author: Minh Nguyen
#Date: 09/22/2023
#Purpose: Python program containing solution to Problem 2
#the first year in which Brutus's balance exceeds Portia's balance

#variables
year = 0

BRUTUS_INITIAL_DEPOSIT = 1
BRUTUS_INTEREST_RATE = 0.05
brutus_balance = BRUTUS_INITIAL_DEPOSIT #this equals 1 in year 0 A.D.

PORTIA_INITIAL_DEPOSIT = 100000
PORTIA_INTEREST_RATE = 0.04
portia_balance = PORTIA_INITIAL_DEPOSIT #this equals 100000 in year 0 A.D.

while brutus_balance <= portia_balance: #determine Brutus's wealth and Portia's wealth in each year up until the first year in which Brutus's balance exceeds Portia's balance.
    year = year + 1

    brutus_balance = brutus_balance * (1 + BRUTUS_INTEREST_RATE)
    brutus_interest_earned = brutus_balance - BRUTUS_INITIAL_DEPOSIT

    portia_balance = portia_balance * (1 + PORTIA_INTEREST_RATE)
    portia_interest_earned = brutus_balance - PORTIA_INITIAL_DEPOSIT

print("At year" + " " + str(year) + ", Brutus's balance exceeds Portia's balance" + ".")
#print the first year in which Brutus's balance exceeds Portia's balance.
print("At year" + " " + str(year) + ", Brutus's balance is" + " " + str(brutus_balance) + " " + "and Portia's balance is" + " " + str(portia_balance) + ".")
#print out that year and the two balances in that year.
print("At year" + " " + str(year) + ", Brutus's interest earned is" + " " + str(brutus_interest_earned) + " " + "and Portia's interest earned is" + " " + str(portia_interest_earned) + ".")
#print the total interest earned by Brutus and Portia by the end of the year in which Brutus's balance exceeds Portia's balance.