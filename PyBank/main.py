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
        
        #row[0].split("-")
        
        # adding all values in profits/losses column to one list
        amount.append(row[1])
        
    # count the total of all of the values in this list aka net total amt of profit/losses
    for t in range(len(amount)):
        netTotal += int(amount[t])
    
    # need to first find changes in profit per period, then calculate average
    # change is the very last value in row[1] minus the first (non-header) value in row[1]
    
    # use lastIndex variable to store the integer to call the last value of the list amount[]
    lastIndex = len(amount) - 1
    # use change variable to hold the difference between the last item in the list and the first item
    change = int(amount[lastIndex]) - int(amount[0])
    # calculate average change
    averageChange = round((change / (totalMonths - 1)),2)
    
    # The greatest increase in profits (date and amount) over the entire period

    # The greatest decrease in profits (date and amount) over the entire period
    
    
    # analysis results should match:
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
    
    # print results to terminal
    print(analysis)


# path for txt file with analysis
file = 'analysis/analysis.txt'
# open text file, write mode
with open(file, 'w') as text:
    # write results into text file
    text.write(analysis)