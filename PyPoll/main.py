#import external directories
import os
import csv

#determine the path to the csv data using a relative address
election_data_csv = os.path.join('Resources','election_data.csv')

#define the variables in the file for reference
ballot_id = election_data_csv[0]
county = election_data_csv[1]
candidate = election_data_csv[2]

#create lists to gather data of each column
ballot_list = []
candidate_list = []

#Read the file and allocate the data into the lists after skipping the header
with open(election_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        ballot_list.append(row[0])
        candidate_list.append(row[2])

#identify the candidates in the election
unique_candidate = []
for x in candidate_list:
    if x not in unique_candidate:
        unique_candidate.append(x)

candidate1=unique_candidate[0]
candidate2=unique_candidate[1]
candidate3=unique_candidate[2]

#determine how many votes are for each candidate
candidate1_votes = [x for x in candidate_list if x == candidate1]
candidate2_votes = [x for x in candidate_list if x == candidate2]
candidate3_votes = [x for x in candidate_list if x == candidate3]

#begin analysis of votes
total_votes = len(ballot_list)
total_candidate1 = len(candidate1_votes)
total_candidate2 = len(candidate2_votes)
total_candidate3 = len(candidate3_votes)
percent_candidate1 = total_candidate1/total_votes
percent_candidate2 = total_candidate2/total_votes
percent_candidate3 = total_candidate3/total_votes

#convert percentages to 2 decimal places
percent_candidate1_dec = round(percent_candidate1*100,2)
percent_candidate2_dec = round(percent_candidate2*100,2)
percent_candidate3_dec = round(percent_candidate3*100,2)

#determine the winner


#Creating variables for the Election Results to keep the format of both outputs the same
title ="Election Results"
space=  "-" *25
result1= f"Total Votes: {total_votes}"
result2= f"{candidate1}: {percent_candidate1_dec}% ({total_candidate1})"
result3 = f"{candidate2}: {percent_candidate2_dec}% ({total_candidate2})"
result4 = f"{candidate3}: {percent_candidate3_dec}% ({total_candidate3}))"
result5 = f"Winner:)"
lines = [title,space,result1,space,result2,result3,result4,space,result5]

#Print output of Election Results to a text file
with open('Analysis/election_results.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')

#Print output of Election Results to the terminal
for line in lines:
    print(line)