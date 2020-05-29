import os
import csv

dataFile = "budget_data.csv"

filePath = os.path.join('Resources', dataFile)

budgetMonth = []
monthPnL = []
monthlyChange = []
totPnL = 0

with open(filePath, 'r') as B_file:
    B_fileData = csv.reader(B_file, delimiter=",") 
    next(B_fileData)  # <-- Header to skip
    for eachMonth in B_fileData:
        # Break into 2 list  
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
import sys

f=open("Analysis_result.txt", "a")
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
