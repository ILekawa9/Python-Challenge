import os

import csv

budget_datacsv = os.path.join('PyBank','Resources', 'budget_data.csv')

months=[]
profit_loss=[]

with open(budget_datacsv) as csvfile:
    csvreader= csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        months.append(row[0])
        profit_loss.append(int(row[1]))

total_months = (len(months))

total_profits = sum(profit_loss)

average_change= (profit_loss[85] - profit_loss[0])/(total_months-1)

profit_change= []

for i in range (1,len(profit_loss)):
    profit_change.append(profit_loss[i]-profit_loss[i-1])
    greatest_increase = max(profit_change)
    greatest_decrease = min(profit_change)

greatest_increase_index = profit_change.index(greatest_increase)
greatest_decrease_index = profit_change.index(greatest_decrease)

greatest_increase_month = months[greatest_increase_index + 1]
greatest_decrease_month = months[greatest_decrease_index + 1]


PyBank_Summary = ["Financial Analysis" '\n',
                  "--------------------------" '\n',
                f'Total Months: {total_months}' '\n',
                f'Total: ${total_profits}''\n',
                f'Average_change: ${average_change:.2f}' '\n',
                f'Greatest Increase in Profits: ${greatest_increase_month}' '\n',
                f'Greatest Decrease in Profits: ${greatest_decrease_month}' '\n']

print(PyBank_Summary)