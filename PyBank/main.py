import os 
import csv

budgetCSV = os.path.join("..", "PyBank", "budget_data.csv")

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

    net_amount = 0
    for amount in profit_losses:
        net_amount += amount
    #print(net_amount)
    #print(profit_losses)

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

    greatest_increase = max(change)
    increase_index = int(change.index(greatest_increase))
    date_increase = date[increase_index + 1]

    #print(date_increase)
    #print(increase_index)
    #print(greatest_increase)

    greatest_decrease = min(change)
    decrease_index = int(change.index(greatest_decrease))
    date_decrease = date[decrease_index + 1]

    #print(date_decrease)
    #print(decrease_index)
    #print(greatest_decrease)

    output = (f"Financial Analysis\n"
        f"----------------------------\n"
        f"Total Months: {total_months}\n"
        f"Total: ${net_amount}\n"
        f"Average Change: ${avg_change}\n"
        f"Greatest Increase in Profits: {date_increase} (${greatest_increase})\n"
        f"Greatest Decrease in Profits: {date_decrease} (${greatest_decrease})")
    print(output)
        
    output_file = open('PyBank_Results.txt', 'w')
    output_file.write(output)