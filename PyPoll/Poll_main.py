#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.

import os
import csv

voterList = []
candiates = []

filePath = os.path.join(".","Resources","election_data.csv")

with open(filePath, 'r') as csvFile:
    elecData = csv.reader(csvFile, delimiter=',')
    for voterID in elecData:
        voterList.append(voterID[0])
        candiates.append(voterID[2])

totalVote = len(voterList)-1
Khan_vote = 0
Correy_vote = 0
Li_vote = 0
OTooley_vote =0 

#Winner finder = sorted[Khan_vote, Correy_vote, Li_vote, OTooley_vote]

#2.eachCandidate = count of each Candidate  
for candidate in candiates:
    if candidate =='Khan':
        Khan_vote +=1
    elif candidate == "Correy":
        Correy_vote +=1
    elif candidate == 'Li':
        Li_vote +=1
    elif candidate == "O'Tooley":
        OTooley_vote += 1

Khan_perc = Khan_vote/totalVote
Correy_perc = Correy_vote/totalVote
Li_perc = Li_vote/totalVote
OTooley_perc = OTooley_vote/totalVote

#https://stackoverflow.com/questions/3121979/how-to-sort-a-list-tuple-of-lists-tuples-by-the-element-at-a-given-index
Results = [("Khan", Khan_vote), ("Correy", Correy_vote), ("Li", Li_vote), ("O'Tooley", OTooley_vote)]
Result_sortedByVote = sorted(Results, key=lambda t:t[1], reverse=True)
#print(Results)
#print(Result_sortedByVote)
winner = Result_sortedByVote[0][0]


print("Election Results")
print("-----------------------------")
print(f"Total Votes: {totalVote} ")
print("-----------------------------")
print(f"Khan : {Khan_perc:.2%}  ({Khan_vote})")
print(f"Correy :  {Correy_perc:.2%}  ({Correy_vote})")
print(f"Li :  {Li_perc:.2%}  ({Li_vote})")
print(f"O'Tooly:  {OTooley_perc:.2%}  ({OTooley_vote})")
print("-----------------------------")
print(f'Winner:  {winner}')
print("-----------------------------")

#Export to txt:  "a" append
import sys
f=open("Election_Results.txt", "a")
sys.stdout = f

print("Election Results")
print("-----------------------------")
print(f"Total Votes: {totalVote} ")
print("-----------------------------")
print(f"Khan : {Khan_perc:.2%}  ({Khan_vote})")
print(f"Correy :  {Correy_perc:.2%}  ({Correy_vote})")
print(f"Li :  {Li_perc:.2%}  ({Li_vote})")
print(f"O'Tooly:  {OTooley_perc:.2%}  ({OTooley_vote})")
print("-----------------------------")
print(f'Winner:  {winner}')
print("-----------------------------")

f.close