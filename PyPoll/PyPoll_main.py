import os
import csv

voterList = []
candiates = []

filePath = os.path.join("Resources","election_data.csv")

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

#eachCandidate = count of each Candidate  
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

Results = [("Khan", Khan_vote), ("Correy", Correy_vote), ("Li", Li_vote), ("O'Tooley", OTooley_vote)]
#Winner finder - sort by vote count by reverse order
Result_sortedByVote = sorted(Results, key=lambda t:t[1], reverse=True)
winner = Result_sortedByVote[0][0]

print("Election Results")
print("---------------------------")
print(f"Total Votes: {totalVote} ")
print("---------------------------")
print(f"Khan :  {Khan_perc:.2%}  ({Khan_vote:,})")
print(f"Correy: {Correy_perc:.2%}  ({Correy_vote:,})")
print(f"Li :    {Li_perc:.2%}  ({Li_vote:,})")
print(f"O'Tooly: {OTooley_perc:.2%}  ({OTooley_vote:,})")
print("---------------------------")
print(f'Winner:  {winner}')
print("---------------------------")

#Export to txt:  "a" append
import sys
f=open("Election_Results.txt", "w")
sys.stdout = f

print("Election Results")
print("---------------------------")
print(f"Total Votes: {totalVote} ")
print("---------------------------")
print(f"Khan :  {Khan_perc:.2%}  ({Khan_vote:,})")
print(f"Correy: {Correy_perc:.2%}  ({Correy_vote:,})")
print(f"Li :    {Li_perc:.2%}  ({Li_vote:,})")
print(f"O'Tooly: {OTooley_perc:.2%}  ({OTooley_vote:,})")
print("---------------------------")
print(f'Winner:  {winner}')
print("---------------------------")

f.close