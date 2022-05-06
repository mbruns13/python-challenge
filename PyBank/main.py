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
    
    # Read the header row first - from class
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
# change is the very last value in row[1] minus the first (non-header) value in row[1]

# use change variable to hold the difference between the last item in the list [-1] and the first item [0]
change = int(amount[-1]) - int(amount[0])
# calculate average change, round to two decimal points
averageChange = round((change / (totalMonths - 1)),2)
    
# The greatest increase in profits (date and amount) over the entire period
greatestIncrease = 0
greatestIncreaseIndex = 0

for i in range(len(amount)):
    currentMonthlyChange = int(amount[i]) - int(amount[i-1])
    if greatestIncrease < currentMonthlyChange:
        greatestIncrease = currentMonthlyChange
        greatestIncreaseIndex = (i)

# The greatest decrease in profits (date and amount) over the entire period
greatestDecrease = 0
greatestDecreaseIndex = 0

for i in range(len(amount)):
    currentMonthlyChange = int(amount[i]) - int(amount[i-1])
    if greatestDecrease > currentMonthlyChange:
        greatestDecrease = currentMonthlyChange
        greatestDecreaseIndex = (i)
    
# analysis results should match:
# Total Months: 86 - DONE
# Total: $22564198 - DONE
# Average Change: $-8311.11 - DONE
# Greatest Increase in Profits: Aug-16 ($1862002) - DONE
# Greatest Decrease in Profits: Feb-14 ($-1825558) - DONE

# setting analysis/results to variable to print and write into the txt file
analysis = f'''Financial Analysis
----------------------------
Total Months: {totalMonths}
Total: ${netTotal}
Average Change: ${averageChange}
Greatest Increase in Profits: {allMonths[greatestIncreaseIndex]} (${greatestIncrease})
Greatest Decrease in Profits: {allMonths[greatestDecreaseIndex]} (${greatestDecrease})'''
    
# print results to terminal
print(analysis)


# path for txt file with analysis
file = 'analysis/analysis.txt'
# open text file, write mode
with open(file, 'w') as text:
    # write results into text file
    text.write(analysis)