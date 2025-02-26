# * You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv).
#   The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`.
#   Your task is to create a Python script that analyzes the votes and calculates each of the following:

#   * The total number of votes cast

#   * A complete list of candidates who received votes

#   * The percentage of votes each candidate won

#   * The total number of votes each candidate won

#   * The winner of the election based on popular vote.

# * As an example, your analysis should look similar to the one below:

#   ```text
#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------
#   ```

# * In addition, your final script should both print the analysis to the terminal and export a text file with the results.

import os
import csv


electionFile_csv = os.path.join('..', 'PyRoll', 'Resources', 'election_data.csv')

def analyze(electionData):
    voterID = []
    candidate = []
    for i in electionData:
        voterID.append(i[0])
        candidate.append(i[2])

#   * The total number of votes cast
    totalVotes = len(voterID)
#   * A complete list of candidates who received votes
    candidateSet = {}
    for j in candidate:
        candidateSet[j] = [0, '']

#   * The percentage of votes each candidate won
    for k in candidate:
        candidateSet[k][0] = candidateSet[k][0] + 1
        #candidateSet[k] = candidateSet[k] + 1
    #candidateWinPerc = {}
    for l in candidateSet:
        candidateSet[l][1] = f"{round((candidateSet[l][0] / totalVotes) * 100, 0):.3f}%"
        #candidateWinPerc[l] = f"{round((candidateSet[l] / totalVotes) * 100, 0):.3f}%"
    
#   * The total number of votes each candidate won
#   * The winner of the election based on popular vote.
    mostVoteCandidate = max(candidateSet, key=candidateSet.get)
    print("Election Results\n-------------------------")
    print(f"Total Votes: {totalVotes}\n-------------------------")
    textInfo = []
    for m in candidateSet:
        print(f"{m}: {candidateSet[m][1]} ({candidateSet[m][0]})")
        textInfo.append(f"{m}: {candidateSet[m][1]} ({candidateSet[m][0]})")
    
    print(f"-------------------------\nWinner: {mostVoteCandidate}\n-------------------------")
        #   Write into text file
    output_file = os.path.join('..', 'PyRoll', 'analysis', 'result.csv')
    with open(output_file, 'w') as resultFile:
        resultFile.write(f"Election Results\n-------------------------\nTotal Votes: {totalVotes}\n-------------------------")
        for n in textInfo:
            resultFile.write(f"\n{n}")
        resultFile.write(f"\n-------------------------\nWinner: {mostVoteCandidate}\n-------------------------")
        resultFile.close()

with open(electionFile_csv, 'r') as csvFile:
    csvreader = csv.reader(csvFile, delimiter=',')
    eader = next(csvreader)
    analyze(csvreader)