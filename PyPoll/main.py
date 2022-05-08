import os
import csv

# path to csv file in resources folder
csvpath = os.path.join('Resources', 'election_data.csv')

ballotID = []
county = []
selectedCandidates = []

# open the file in "read" mode ('r') and store the contents in the variable "text"
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Read the header row first - from class
    csv_header = next(csvreader)

    for row in csvreader:
        ballotID.append(row[0])
        county.append(row[1])
        selectedCandidates.append(row[2])

# The total number of votes cast
totalVotes = len(ballotID)

# A complete list of candidates who received votes
# sorting candidates alphabetically in new list
sortedSelectedCandidates = []
sortedSelectedCandidates.extend(selectedCandidates)
sortedSelectedCandidates.sort()
# new list to contain the name of each candidate voted for
candidateList = []
for c in range(len(sortedSelectedCandidates)):
    if sortedSelectedCandidates[c] != sortedSelectedCandidates[c-1]:
        candidateList.append(sortedSelectedCandidates[c])
#print(candidateList) - checked, prints three names so will call index values 0, 1, and 2

# The total number of votes each candidate won
candidate0Votes = selectedCandidates.count(candidateList[0])
candidate1Votes = selectedCandidates.count(candidateList[1])
candidate2Votes = selectedCandidates.count(candidateList[2])

# The percentage of votes each candidate won
candidate0Percentage = round(((candidate0Votes / totalVotes) * 100),3)
candidate1Percentage = round(((candidate1Votes / totalVotes) * 100),3)
candidate2Percentage = round(((candidate2Votes / totalVotes) * 100),3)

# The winner of the election based on popular vote
winner = ""
if candidate0Votes > candidate1Votes and candidate0Votes > candidate2Votes:
    winner = candidateList[0]
elif candidate1Votes > candidate0Votes and candidate1Votes > candidate2Votes:
    winner = candidateList[1]
elif candidate2Votes > candidate0Votes and candidate2Votes > candidate1Votes:
    winner = candidateList[2]

#print(winner) - checked

# Your analysis should look similar to the following:

    # Election Results
    # -------------------------
    # Total Votes: 369711 - DONE
    # -------------------------
    # Charles Casper Stockham: 23.049% (85213) - DONE
    # Diana DeGette: 73.812% (272892) - DONE
    # Raymon Anthony Doane: 3.139% (11606) - DONE
    # -------------------------
    # Winner: Diana DeGette - DONE
    # -------------------------

# setting analysis/results to variable to print and write into the txt file
analysis = f'''Election Results
-------------------------
Total Votes: {totalVotes}
-------------------------
{candidateList[0]}: {candidate0Percentage}% ({candidate0Votes})
{candidateList[1]}: {candidate1Percentage}% ({candidate1Votes})
{candidateList[2]}: {candidate2Percentage}% ({candidate2Votes})
-------------------------
Winner: {winner}
-------------------------'''
    
# print results to terminal
print(analysis)

# path for txt file with analysis
file = 'analysis/analysis.txt'
# open text file, write mode
with open(file, 'w') as text:
    # write results into text file
    text.write(analysis)