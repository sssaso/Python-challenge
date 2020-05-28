# Import csv file with test file
import os
import csv

DataDir = "G:/12.Data/DataAnalyticsBootCamp/Unit3_Python/Homework/Instructions/PyBank/Resources/"
DataFile = "budget_data_test.csv"

budgetMonth = []
monthPnL = []
monthlyChange = []
totPnL = 0

with open(DataDir+DataFile, 'r') as B_file:
    #B_fileData = B_file.read()  
    B_fileData = csv.reader(B_file, delimiter=",") 
    next(B_fileData)  # <-- Header
    for eachMonth in B_fileData:
        budgetMonth.append(eachMonth[0])
        monthPnL.append(int(eachMonth[1]))

for i, pnl in enumerate(monthPnL):
    if i+1 >= len(monthPnL):
        break
    mChange = monthPnL[i+1]-monthPnL[i]
    monthlyChange.append(mChange)
    #print(mChange)

#print(monthlyChange) 
#print(budgetMonth)
#print(monthPnL)

# Unzip into 2 list  - done

TotalMonth = len(budgetMonth)
TotalPnL = sum(monthPnL)
avgChange = sum(monthlyChange) / len(monthlyChange)

print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {TotalMonth}")
print(f"Total PnL: $ {TotalPnL:,}")
print(f"Average Change: ${avgChange:,.2f}")



#How to convert data into List or Dict or Set? like  [(Jan-10,867884), (Feb-10,984655),,,]
# what is data type when import csv ?  List

# 1. Total numer of months  --> len of Date column?  - done
# 2. Net total amount of P&L over the entire period -done
# 3. Average change of the changes in P&L over the entire period - done 
# 4. The greatest increase in Profits (date and amount) over the entire period
# 5. The greatest decrease in Losses (date and amount) over the entire period
# 6. Print analysis to the terminal abd export a text file with results