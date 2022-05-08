import os
import csv

# path to csv file in resources folder
csvpath = os.path.join('Resources', 'election_data.csv')

# creating empty lists to add to when reading in csv file
ballotID = []
county = []
selectedCandidates = []

# creating empty dictionary to fill in with candidate name and votes
candidateVotes = {}

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
for c in range(len(selectedCandidates)):
    # if candidate name is already a key in dict, add one to its value
    candidateVotes[selectedCandidates[c]] = candidateVotes.get(selectedCandidates[c],0) + 1

# place candidate names into list 'candidates'
candidates = list(candidateVotes.keys())
# place votes per candidate into list 'votes'
votes = list(candidateVotes.values())
percentage = []

# calculating percentage of total votes for each candidate
for i in range(len(votes)):
    percentage.append(round(((votes[i] / totalVotes)*100), 3))
    
maxVotes = 0
maxIndex = 0
# finding max number of votes in list of total votes per candidate
for i, n in enumerate(votes):
    if maxVotes == 0 or n > maxVotes:
        maxVotes = n
        maxIndex = i
# using the index of the max value in votes to id the candidate with the corresponding max number of votes
winner = candidates[maxIndex]

print("Election Results")
print("-------------------------")
print(f"Total Votes: {totalVotes}")
print("-------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {percentage[i]}% ({votes[i]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")


# path for txt file with analysis
file = 'analysis/analysis.txt'
# open text file, write mode
with open(file, 'w') as text:
    # write results into text file
    text.write("Election Results\n")
    text.write("-------------------------\n")
    text.write(f"Total Votes: {totalVotes}\n")
    text.write("-------------------------\n")
    for i in range(len(candidates)):
        text.write(f"{candidates[i]}: {percentage[i]}% ({votes[i]})\n")
    text.write("-------------------------\n")
    text.write(f"Winner: {winner}\n")
    text.write("-------------------------")