# Importing modules os and csv

import os
import csv

# Defining the variables / dictionaries

vote_total = 0
candidates_votes = {}
winner_count = 0
winner_name = ""

# Opening the file and getting this show on the road!

with open('election_data.csv', newline = '') as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ',')
    print(csvreader)
    csv_header = next(csvreader)
    for row in csvreader:

        # Increasing vote by 1 per row

        vote_total += 1

        # If the candidate's name is already a dictionary within candidates_votes, then the votes
        # for that candidate will be increased by 1
        # Otherwise, it will add the new candidate with a vote value of 1

        if row[2] in candidates_votes:
            candidates_votes[row[2]]['votes'] += 1
        else:
            candidates_votes[row[2]] = {}
            candidates_votes[row[2]]['name'] = row[2]
            candidates_votes[row[2]]['votes'] = 1

# Generating the text file

with open('pypoll.txt','w') as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")

    # Printing the total number of votes

    file.write("Total Votes: " + str(vote_total) + "\n")
    file.write("-------------------------\n")

    # For loop - this extracts the candidate information (name and votes), as well as calculating
    # the percentage of votes acquired

    for candidate_id, candidate_info in candidates_votes.items():
        file.write(candidate_info['name'] + ": " + str(round((candidate_info['votes']/int(vote_total))*100,2)) + "00%" + " (" + str(candidate_info['votes']) + ")" + "\n")
        
        # This checks against winner_count to see if the candidate's votes are greater than 
        # the current value in winner_count. Winner_count is defaulted to 0 to start and is
        # populated with the first record it encounters. winner_name is for the winner's name
        # and is extracted at the same time
        
        if candidate_info['votes'] > winner_count:
            winner_count = candidate_info['votes']
            winner_name = candidate_info['name']
    file.write("-------------------------\n")

    # Printing the winner's name
    
    file.write("Winner: " + str(winner_name) + "\n")
    file.write("-------------------------\n")

# Printing to terminal by opening the generated pypoll.txt file and printing the results directly

with open('pypoll.txt') as file:
    for line in file:
        print(line, end='')