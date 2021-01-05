#!/usr/bin/env python
# coding: utf-8

# # Python Bank

# **Main script**

# In[35]:


# File path across OS
import os

# Module for reading CSV files
import csv

#parameters
profit_loss=[]
months_list=[]
change_list=[]
months_change_list=[]
add=0
total=0
total_months=0
greatest_increase=[' ',0]
greatest_decrease=[' ',0]

#text file

file = './Analysis/Analysis.txt'

#specifying the path
csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
   
    #checking the read by printing the header
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    
    #calculated total_months, net_profit and loss and created lists
    for row in csvreader:
        total_months=total_months+1
        total=total+int(row[1])
        months_list.append(row[0])
        profit_loss.append(row[1])  
    
    #created net_change_list and months_list
    for num in range(1,len(profit_loss)):
        num_1=int(profit_loss[num-1])
        num_2=int(profit_loss[num])
        change=num_2-num_1
        change_list.append(change)
        months_change_list.append(months_list[num])
        
    #found average,greatest increase and decrease   
    for i in range(0,len(change_list)):
        add=add+change_list[i]
        if(greatest_increase[1]<change_list[i]):
            greatest_increase[0]=months_change_list[i]
            greatest_increase[1]=change_list[i]
        if(greatest_decrease[1]>change_list[i]):
            greatest_decrease[0]=months_change_list[i]
            greatest_decrease[1]=change_list[i]
    
    #printing
    Analysis=("\nFinancial Analysis\n"+"======================\n"+"Total Months: "+ str(len(months_list))+"\n"+"Total: $"+str(total)
           +"\n"+"Average Change: $"+ str(round(add/len(change_list),2))+"\n"+"Greatest increase in profits: "+ str(greatest_increase[0])
             + ", ($"+ str(greatest_increase[1])+")"+"\nGreatest decrease in profits: "+ str(greatest_decrease[0])
             + ", ($"+ str(greatest_decrease[1])+")")
    print(Analysis)
    
    #writing to file
    with open(file, 'w') as text:
        text.write(Analysis)
         

