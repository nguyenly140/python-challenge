# * Your task is to create a Python script that analyzes the records to calculate each of the following:

#   * The total number of months included in the dataset

#   * The net total amount of "Profit/Losses" over the entire period

#   * Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

#   * The greatest increase in profits (date and amount) over the entire period

#   * The greatest decrease in profits (date and amount) over the entire period

# * As an example, your analysis should look similar to the one below:

#   ```text
#   Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $38382578
#   Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)
#   ```

# * In addition, your final script should both print the analysis to the terminal and export a text file with the results.
import os
import csv

budgetData_csv = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')
def analyze(budgetData):
#   * The total number of months included in the dataset
    months = []
    profit_loss = []
    for row in budgetData:
        months.append(row[0])
        profit_loss.append(row[1])
    totalMonths = len(months)
#   * The net total amount of "Profit/Losses" over the entire period
    total = 0
    num = 0
    change = 0
    totalChange = 0.00
    greatestInc = 0
    greatestDec = 0
    for i in range(len(profit_loss)):
        
        total += int(profit_loss[i])

        if num != 0:
            change = (int(profit_loss[i]) - num)
            totalChange += change
            if change > greatestInc:
                greatestInc = change
                greatestIncMonth = months[i]
            elif change < greatestDec:
                greatestDec = change
                greatestDecMonth = months[i]
            #print(f"{change} = {int(i)} - {num}")
        num = int(profit_loss[i])
    print(f"Total Months: {len(months)}")
    print(f"Total: ${total}")
#   * Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
    totalChange = "{:.2f}".format(totalChange/len(months))
    print(f"Average Change: ${totalChange}")
#   * The greatest increase in profits (date and amount) over the entire period
    print(f"Greatest Increase in Profits: {greatestIncMonth} (${greatestInc})")
#   * The greatest decrease in profits (date and amount) over the entire period
    print(f"Greatest Decrease in Profits: {greatestDecMonth} (${greatestDec})")
with open(budgetData_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    analyze(csvreader)