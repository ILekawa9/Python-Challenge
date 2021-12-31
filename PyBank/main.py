import os

import csv

budgetdatapath = os.path.join('Resources', 'budget_data.csv')

with open(budgetdatapath) as csvbudgetfile:
    csvreader = csv.reader(csvbudgetfile, delimiter=',')
 
csv_header = next(csvbudgetfile)

lines = len(list(csvreader))





print (total)