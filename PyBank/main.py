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
    #print(total_months)
    #print(date)

#The net total amount of "Profit/Losses" over the entire period
    #add all numbers in column 2 and assign net total
    net_amount = 0
    for amount in profit_losses:
        net_amount += amount
    #print(net_amount)
    #print(profit_losses)

#The average of the changes in "Profit/Losses" over the entire period
    change = []
    last_row = profit_losses[0]
    for amount in profit_losses:
        new_amount = amount - last_row
        change.append(new_amount)
        last_row = amount

    change.pop(0)
    avg_change = round(sum(change) / len(change), 2)
    #print(avg_change)
    #print(change)

#The greatest increase in profits (date and amount) over the entire period
    greatest_increase = max(change)
    increase_index = int(change.index(greatest_increase))
    date_increase = date[increase_index + 1]
    #print(date_increase)
    #print(increase_index)
    #print(greatest_increase)

#The greatest decrease in losses (date and amount) over the entire period
    greatest_decrease = min(change)
    decrease_index = int(change.index(greatest_decrease))
    date_decrease = date[decrease_index + 1]
    #print(date_decrease)
    #print(decrease_index)
    #print(greatest_decrease)

#In addition, your final script should both print the analysis to the terminal and export a text file with the results.
    def print_results():
        print("Financial Analysis")
        print("----------------------------")
        print(f"Total Months: {total_months}")
        print(f"Total: ${net_amount}")
        print(f"Average Change: ${avg_change}")
        print(f"Greatest Increase in Profits: {date_increase} (${greatest_increase})")
        print(f"Greatest Decrease in Profits: {date_decrease} (${greatest_decrease})")
    print_results()

output_file = open('PyBank_Results.txt', 'w')
output_file.write(f"Financial Analysis\n" 
    "----------------------------\n"
    "Total Months: " {total_months})
    #"Total: ${net_amount}\n"
    #"Average Change: ${avg_change}\n"
    #"Greatest Increase in Profits: {date_increase} (${greatest_increase})\n"
    #"Greatest Decrease in Profits: {date_decrease} (${greatest_decrease})")