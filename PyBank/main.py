import os 
import csv

budgetCSV = os.path.join("..", "PyBank", "budget_data.csv")


#Your task is to create a Python script that analyzes the records to calculate each of the following:
#The total number of months included in the dataset
    #Count number of rows in column 1 and skip the header, attach to number of months
date = []
profit_loss = []

with open(budgetCSV, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    next(csv_reader, None)
    for row in csv_reader:
        date.append(row[0])
        profit_loss.append(int(row[1]))

print(len(date))

#The net total amount of "Profit/Losses" over the entire period
    #add all numbers in column 2 and assign net total
total = 0
for transaction in profit_loss:
    total += transaction
print(total)

#The average of the changes in "Profit/Losses" over the entire period
    #divide net total by number of months

change = []
total2 = 0
for transaction in profit_loss:
    total2 -= transaction
    change.append(total2)
avgchange = sum(change) / len(change)
print(avgchange)

#The greatest increase in profits (date and amount) over the entire period
    #loop through each row, potentially use a max function

#The greatest decrease in losses (date and amount) over the entire period
    #loop through each row, potentially use a min function

#In addition, your final script should both print the analysis to the terminal and export a text file with the results.






