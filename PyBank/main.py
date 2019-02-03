import os 
import csv

budgetCSV = os.path.join("..", "PyBank", "budget_data.csv")


#Your task is to create a Python script that analyzes the records to calculate each of the following:
#The total number of months included in the dataset
    #Count number of rows in column 1 and skip the header, attach to number of months
date = []
profit_losses = []

with open(budgetCSV, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    next(csv_reader, None)
    for row in csv_reader:
        date.append(row[0])
        profit_losses.append(int(row[1]))
    total_months = len(date)
    print(total_months)
    #print(date)

#The net total amount of "Profit/Losses" over the entire period
    #add all numbers in column 2 and assign net total
    net_amount = 0
    for amount in profit_losses:
        net_amount += amount
    print(net_amount)
    #print(profit_losses)

#The average of the changes in "Profit/Losses" over the entire period
    change = []
    last_row = profit_losses[1]
    for amount in profit_losses:
        new_amount = amount - last_row
        change.append(new_amount)
        last_row = amount

    print(change)
    #avgchange = sum(change) / len(change)
    #print(avgchange)

#The greatest increase in profits (date and amount) over the entire period
    #loop through each row, potentially use a max function

#print(max(change))

#The greatest decrease in losses (date and amount) over the entire period
    #loop through each row, potentially use a min function

#print(min(change))

#In addition, your final script should both print the analysis to the terminal and export a text file with the results.

#total_months = skip header, count number of rows


#net_amount = 
#avg_change = 
#greatest_increase = 
#greatest_decrease = 
