# import libraries
import os
import csv

# set path to read in and output election data files
election_data_in = os.path.join("/Users/masterambassador/PycharmProjects/Python Challenge/Pypoll/election_data.csv")
Election_out = os.path.join("/Users/masterambassador/PycharmProjects/Python Challenge/Pypoll/election_an.txt")

# Total Vote Counter
vote_talley = 0

# Declare empty List to hold candidates and dictionary of key:candidate value: vote
candidates = []
vote_counter = {}
counter = 0

# Winning Candidate and Winning Count Tracker
winner = ""
final_talley = 0

# Read the csv and convert it into a list of dictionaries
with open(election_data_in) as election_data:
    reader = csv.reader(election_data)

    # declare first line as header to exclude from calculations
    header = next(reader)

    # Begin loop to iterate through lists
    for row in reader:

        # Run the loader animation, this modification, prints the loader animiation only once
        # Prior loader iterated through file and printed a dot for each
        if ((counter % 300000) == 0):
            print( "Processing... \n" )

        # Cumulative vote counter
        vote_talley = vote_talley + 1

        # Extract candidate name from third row value in csv file
        candidate_name = row[2]

        # Loop through candidates identifying each unique candidate discovered
        if candidate_name not in candidates:

            # Append each unique candidate encountered to running list
            candidates.append(candidate_name)

            # And begin tracking that candidate's voter count
            vote_counter[candidate_name] = 0

        # Then add a vote to that candidate's count
        vote_counter[candidate_name] = vote_counter[candidate_name] + 1
        counter += 1

# Print the results and export the data to our text file
with open(Election_out, "w") as election_txt:

    # Print the final vote count (to terminal)
    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {vote_talley}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # Save the final vote count to the text file
    election_txt.write(election_results)

    # Determine the winner by looping through the counts
    for candidate in vote_counter:

        # Retrieve vote count and percentage using float to enable decimals
        votes = vote_counter.get(candidate)
        vote_percentage = float(votes) / float(vote_talley) * 100

        # Determine winning vote count and candidate
        if (votes > final_talley):
            final_talley = votes
            winner = candidate

        # Print each candidate's voter count and percentage (to terminal)
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")

        # Save each candidate's voter count and percentage to text file
        election_txt.write(voter_output)

    # Display Election Results for Winner
    Winner_Performance = (
        f"-------------------------\n"
        f"Winner: {winner}\n"
        f"-------------------------\n")
    print(Winner_Performance)

    # Save the winning candidate's name to the text file
    election_txt.write(Winner_Performance)