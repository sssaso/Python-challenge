import os
import csv

# myDir = "/Users/JJ/Documents/GitHub/Python-challenge/PayBank/Resources/" # works
myDir = "C:/Users/JJ/Documents/GitHub/Python-challenge/PayBank/Resources/" # works
myFile = "budget_data_test.csv"

csvPath = os.path.join(myDir, myFile) 
# csvPath = os.path.join(".","Resources/", "budget_data_test.csv" ) # works fine

with open(csvPath) as csvFile:
    budgetData = csv.reader(csvFile, delimiter= ',')

    for line in budgetData:
        print(line)

