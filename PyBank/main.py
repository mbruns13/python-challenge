# In this challenge, you are tasked with creating a Python script to analyze the financial 
# records of your company. You will give a set of financial data called budget_data.csv. 
# The dataset is composed of two columns: "Date" and "Profit/Losses". 
# (Thankfully, your company has rather lax standards for accounting, so the records are simple.)

# Your task is to create a Python script that analyzes the records to calculate each of the following:
import os
import csv

# path to csv file in resources folder
csvpath = os.path.join('Resources', 'budget_data.csv')

# variables/lists to store data from csv file
allMonths = []
amount = []
netTotal = 0

# open the file in "read" mode ('r') and store the contents in the variable "text"
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #print(csvreader)
    
    # Read the header row first - from class - need?
    csv_header = next(csvreader)

    for row in csvreader:
        # adding all cells in date column to one list
        allMonths.append(row[0])
        # count the number of values from the date column
        totalMonths = len(allMonths)
        
        # adding all values in profits/losses column to one list
        amount.append(row[1])
        
    # count the total of all of the values in this list aka net total amt of profit/losses
    for t in range(len(amount)):
        netTotal += int(amount[t])
    
    # need to first find changes in profit per period, then calculate average
    averageChange = 0
    
    # The greatest increase in profits (date and amount) over the entire period

    # The greatest decrease in profits (date and amount) over the entire period
    
    
    # print results to terminal - results should match:
    # Total Months: 86 - DONE
    # Total: $22564198 - DONE
    # Average Change: $-8311.11
    # Greatest Increase in Profits: Aug-16 ($1862002)
    # Greatest Decrease in Profits: Feb-14 ($-1825558)

    analysis = f'''Financial Analysis
----------------------------
Total Months: {totalMonths}
Total: ${netTotal}
Average Change: ${averageChange}
Greatest Increase in Profits: ($)
Greatest Decrease in Profits: ($) '''
    
    print(analysis)


# path for txt file with analysis
file = 'analysis/analysis.txt'
# open text file, write mode
with open(file, 'w') as text:
    text.write(analysis)