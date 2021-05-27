# Import dependencies
import os
import csv

# Open and read csv file
path = os.path.join('.', 'Resources', 'budget_data.csv')

# Declare initial variables
months = 0
net_total = 0
initial = 0
changes = []
dates = []
sum_changes = 0

with open(path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")

    # Skip the header so it is omitted
    next(csv_reader)

    for row in csv_reader:
        # Count the total number of months included in the dataset
        months = months + 1

        # Calculate the net total amount of "Profit/Losses" over the entire period
        net_total = net_total + int(row[1])

        # Calculate the changes in "Profit/Losses" over the entire period
        final = int(row[1])
        changes.append(final - initial)
        initial = final

        # Append the date to an array
        dates.append(row[0])

    # Find the average of these changes
    del changes[0]
    for i in changes:
        sum_changes = sum_changes + i

    average_change = round(sum_changes / len(changes), 2)

    # Find the greatest increase in profits
    top_profit = max(changes)
    index_profit = changes.index(top_profit)

    # Find the greatest decrease in losses
    top_loss = min(changes)
    index_loss = changes.index(top_loss)        
      
    print("")
    print("Financial Analysis")
    print("------------------")
    print("Total months:", months)
    print(f"Total: ${net_total}")
    print(f"Average Change : ${average_change}")
    print(f"Greatest Increase in Profits: {dates[index_profit]} (${top_profit})")
    print(f"Greatest Decrease in Profits: {dates[index_loss]} (${top_loss})")
    print("")

    # Open and read csv file
    write_path = os.path.join('.', 'Analysis', 'analysis.txt')
    with open(write_path, "w+") as output:
        output.write("Financial Analysis\n")
        output.write("------------------\n")
        output.write(f"Total months:{months}\n")
        output.write(f"Total: ${net_total}\n")
        output.write(f"Average Change : ${average_change}\n")
        output.write(f"Greatest Increase in Profits: {dates[index_profit]} (${top_profit})\n")
        output.write(f"Greatest Decrease in Profits: {dates[index_loss]} (${top_loss})\n")