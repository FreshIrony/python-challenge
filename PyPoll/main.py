import os 
import csv

budgetCSV = os.path.join("..", "PyPoll", "election_data.csv")


#You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. 
#Your task is to create a Python script that analyzes the votes and calculates each of the following:

#The total number of votes cast
voter_id = []
county = []
candidate = []

with open(budgetCSV, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    next(csv_reader, None)
    for row in csv_reader:
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
    total_votes = len(voter_id)
    print(total_votes)
    #print(voter_id)
    #print(county)
    #print(candidate)

#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.