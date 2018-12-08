import os
import csv

csvpath = os.path.join("election_data.csv")

TotalCand = []
Votes = []
UniquCand = []

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    
    for row in csvreader:
        #Puts all the Voters and candidates into a list
        TotalCand.append(row[2])        
    poll = open("poll_data.txt","w+")    
    poll.write("Election Results")
    poll.write("\n")
    poll.write("----------------------------")
    poll.write("\n")
    poll.write("Total votes: " + str(len(TotalCand)))
    poll.write("\n")
    poll.write("----------------------------")
    poll.write("\n")
    
# prints out the header and the total number of votes
    print("Election Results")
    print("----------------------------")
    print("Total votes: " + str(len(TotalCand)))
    print("----------------------------")

#creates a unique list of candidates
#based on the order of the list of candidates the loop counts how many votes for each candidate
    UniqueCand = list(set(TotalCand))
    for i in range(len(UniqueCand)):
        Votes.append(TotalCand.count(UniqueCand[i]))
        print(UniqueCand[i] + ": " + str(format(Votes[i]/len(TotalCand),".0%")) + " (" + str(Votes[i])+ ")")
        poll.write(UniqueCand[i] + ": " + str(format(Votes[i]/len(TotalCand),".0%")) + " (" + str(Votes[i])+ ")")
        poll.write("\n")
    print("----------------------------")
    poll.write("----------------------------")
    poll.write("\n")
#this find the highest value in the list Votes and then finds the index and searches in the Unique Cand list for the name
    Winner = UniqueCand[Votes.index(max(Votes))]
    print("Winner: " + Winner)
    print("----------------------------")
    
    poll.write("Winner: " + Winner)
    poll.write("\n")
    poll.write("----------------------------")    
    poll.close()