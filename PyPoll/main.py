import os
import csv

election_csv = os.path.join("..", "PyPoll", "election_data.csv")

voter_id = []
county = []
candidates = []

with open(election_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader, None)
    for row in csvreader:
        voter_id.append(row[0])
        county.append(row[1])
        candidates.append(row[2])
    
unique_candidates = list(sorted(set(candidates)))
#print(unique_candidates)
    
total_votes = len(voter_id)
#print(total_votes)

votes_won = []
for candidate in unique_candidates:
    votes_won.append(candidates.count(candidate))
#print(votes_won)

percent_won = []
for votes in votes_won:
    percent = (votes / total_votes) * 100
    percent_won.append(round(percent, 2))
#print(percent_won)

standings = zip(unique_candidates, percent_won, votes_won)
sorted_standings = sorted(standings, key=lambda x: int(x[2]), reverse = True)
#print(sorted_standings)

election_results = (f"Election Results\n"
                    "-------------------------\n"
                    f"Total Votes: {total_votes}\n"
                    f"-------------------------\n"
                    f"{sorted_standings[0][0]}: {sorted_standings[0][1]}% ({sorted_standings[0][2]})\n"
                    f"{sorted_standings[1][0]}: {sorted_standings[1][1]}% ({sorted_standings[1][2]})\n"
                    f"{sorted_standings[2][0]}: {sorted_standings[2][1]}% ({sorted_standings[2][2]})\n"
                    f"{sorted_standings[3][0]}: {sorted_standings[3][1]}% ({sorted_standings[3][2]})\n"
                    f"-------------------------\n"
                    f"Winner: {sorted_standings[0][0]}\n"
                    f"-------------------------")

print(election_results)

output_file = open('PyPoll_Results.txt', 'w')
output_file.write(election_results)