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

#calculate the monthly change in profits
monthly_change = [profit_loss_list[i+1]-profit_loss_list[i] for i in range(len(profit_loss_list)-1)]

#complete analysis calculations
total_months= len(months_list)
total_profit_loss = sum(profit_loss_list)
average_change = sum(monthly_change)/len(monthly_change)

#convert average change to a 2 decimal integer
avg_chng_dec= round(average_change,2)

#determine which months are the max & min monthly change
increase_profits = max(monthly_change)
decrease_profits = min(monthly_change)

#getting the index of the max & min of the monthly change
#the index is +1 to account for the one item that is dropped when calculating difference
increase_index = monthly_change.index(increase_profits)+1
decrease_index = monthly_change.index(decrease_profits)+1

#use the indices to get the related months of the movements
increase_month = months_list[increase_index]
decrease_month= months_list[decrease_index]


#Creating variables for the Financial Analysis output to keep both outputs the same
title ="Financial Analysis"
space=  "-" *25
result1= f"Total Months: {total_months}"
result2= f"Total: ${total_profit_loss}"
result3 = f"Average Change: ${avg_chng_dec}"
result4 = f"Greatest Increase in Profits: {increase_month} (${increase_profits})"
result5 = f"Greatest Decrease in Profits: {decrease_month} (${decrease_profits})"
lines = [title,space,result1,result2,result3,result4,result5]

#Print output of Financial Analysis to a text file
with open('Analysis/readme.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')

#Print output of Financial Analysis to the terminal
for line in lines:
    print(line)