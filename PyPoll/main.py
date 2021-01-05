#!/usr/bin/env python
# coding: utf-8

# # Python Poll

# **Polling Analysis**

# In[31]:


# File path across OS
import os

# Module for reading CSV files
import csv

#parameters
candidates_list=[]
total_dict={}
winner=0
total_votes=0
winnername=''

#text file

file = './Analysis/Analysis.txt'

#specifying the path
csvpath = os.path.join('.', 'Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
   
    # checking the read by printing the header
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    
    # iterating over the rows to find all the unique candidates
    for row in csvreader:
        total_votes=total_votes+1
        if row[2] not in candidates_list:
            candidates_list.append(row[2])
            total_dict[row[2]]=0
        # finding the votes count for the candidates
        total_dict[row[2]]=total_dict[row[2]]+1 
    # printing the results and writing to text file
    with open(file, 'w') as text:
        # printing total votes
        Total_votes_print=("Election Results\n"+"-------------------------\n"+"Total Votes: "+str(total_votes)+"\n-------------------------")
        print(Total_votes_print)
        text.write(Total_votes_print)
        # iterating over the dictionary to print the results
        for x,y in total_dict.items():
            candidates=("\n"+x+": "+str(round((y/total_votes)*100,4))+"00% ("+str(y)+")")
            print(candidates)
            text.write(candidates)
            # finding the winner
            if(y>winner):
                winner=y
                winnername=x
        # printing the winner
        winnerprint=("\n-------------------------\nWinner: "+ winnername + "\n-------------------------")
        print(winnerprint)
        text.write(winnerprint)
    
    


# In[ ]:




