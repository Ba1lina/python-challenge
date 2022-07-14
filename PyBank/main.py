#import external directories
import os
import csv

#determine the path to the csv data using a relative address
budget_data_csv = os.path.join('Resources','budget_data.csv')

#define the variables in the file
date = budget_data_csv[0]
monthly_profit_loss = budget_data_csv[1]

#create lists to gather data of each column
months_list = []
profit_loss_list = []

#Read the file and allocate the data into the lists after skipping the header
with open(budget_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        months_list.append(row[0])
        profit_loss_list.append(row[1])

#convert the profit and loss list into integers for further evaluation
profit_loss_list = [int(i) for i in profit_loss_list]

#complete initial calculations @TODO average change needs to have two decimals places
total_months= len(months_list)
total_profit_loss = sum(profit_loss_list)
average_change = total_profit_loss/total_months
#increase_profits = X
#increase_month = a
#decrease_profits = y
#decrease_month=b

title ="Testing Analysis"
space=  "-" *25
result1= f"Total Months: {total_months}"
result2= f"Total: ${total_profit_loss}"
result3 = f"Average Change: ${average_change}"
result4 = f"Greatest Increase in Profits: "
result5 = f"Greatest Decrease in Profits: "

#Print output of Financial Analysis
lines = [title,space,result1,result2,result3,result4,result5]
with open('Analysis/readme.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')
