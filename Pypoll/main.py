# PyPoll

import os
import csv

election_data_csv = os.path.join("resources", "election_data.csv")


# open file
with open(election_data_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    header = next(csv_reader)

    print('Election Results')
    print('-------------------------')

# declaring variables 
    votetotal = 0
    vote_candidate = {}
    list_candidate = []
    winningcount = 0
    winner = ""

    for row in csv_reader:
        # total votes
        votetotal = votetotal + 1
        #  finding which candidate got votes
        candidate_name = row[2]
        if candidate_name not in list_candidate:
            # adding candidates to the list
            list_candidate.append(candidate_name)
            vote_candidate[candidate_name] = 0
        # pairing candidate with how many votes they got
        vote_candidate[candidate_name] = vote_candidate[candidate_name] + 1

    print(f'Total votes: {votetotal}')
    print('----------------------')

    # finding the percentage of votes
    for candidate in vote_candidate:
        votes = vote_candidate.get(candidate)
        vote_percentage = float(votes) / float(votetotal) * 100

        if (votes > winningcount):
            winningcount = votes
            winner = candidate

        voter_output = f'{candidate}: {vote_percentage:3f}% ({votes})'

    print(voter_output)

    print('------------------------')

    print(f'Winner: {winner}')