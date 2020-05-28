# os.join.path    
import os
import csv

fileDir = "/Users/JJ/Documents/GitHub/Python-challenge/PyBank/Resources/"
dataFile = "budget_data.csv"

filePath = os.path.join(fileDir, dataFile)

budgetMonth = []
monthPnL = []
monthlyChange = []
totPnL = 0

with open(filePath, 'r') as B_file:
    #B_fileData = B_file.read()  
    B_fileData = csv.reader(B_file, delimiter=",") 
    next(B_fileData)  # <-- Header to skip
    for eachMonth in B_fileData:
        # Unzip into 2 list  
        budgetMonth.append(eachMonth[0])
        monthPnL.append(int(eachMonth[1]))

for i, pnl in enumerate(monthPnL):
    if i+1 >= len(monthPnL):
        break
    mChange = monthPnL[i+1]-monthPnL[i]
    monthlyChange.append(mChange)

TotalMonth = len(budgetMonth)
TotalPnL = sum(monthPnL)
avgChange = sum(monthlyChange) / len(monthlyChange)
gIncrease = max(monthlyChange)
gIncMonth = monthlyChange.index(gIncrease)+1
gDecrease = min(monthlyChange)
gDecMonth = monthlyChange.index(gDecrease)+1

print("Financial Analysis" )
print("----------------------------------------")
print(f"Total Months: {TotalMonth}")
print(f"Total PnL: $ {TotalPnL:,}")
print(f"Average Change: ${avgChange:,.2f}")
print(f"Great Increase : {budgetMonth[gIncMonth]} $ {gIncrease:,}")
print(f"Great Decrease : {budgetMonth[gDecMonth]} ${gDecrease:,}")
print("----------------------------------------")

#export to txt 
# https://stackoverflow.com/questions/36571560/directing-print-output-to-a-txt-file-in-python-3/36571602

import sys

f=open("Analysis_OP.txt", "a")
sys.stdout = f

print("Financial Analysis")
print("----------------------------------------")
print(f"Total Months: {TotalMonth}")
print(f"Total PnL: $ {TotalPnL:,}")
print(f"Average Change: ${avgChange:,.2f}")
print(f"Great Increase : {budgetMonth[gIncMonth]} $ {gIncrease:,}")
print(f"Great Decrease : {budgetMonth[gDecMonth]} ${gDecrease:,}")
print("----------------------------------------")

f.close


#How to convert data into List or Dict or Set? like  [(Jan-10,867884), (Feb-10,984655),,,]
# what is data type when import csv ?  List

# 1. Total numer of months  --> len of Date column?  - done
# 2. Net total amount of P&L over the entire period -done
# 3. Average change of the changes in P&L over the entire period - done 
# 4. The greatest increase in Profits (date and amount) over the entire period
# 5. The greatest decrease in Losses (date and amount) over the entire period
# 6. Print analysis to the terminal abd export a text file with results