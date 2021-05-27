# Import dependencies
import os
import csv

# Open and read csv file
path = os.path.join('.', 'Resources', 'election_data.csv')

# Declare initial variables
total_votes = 0
candidates = []
loop_num = 0
vote_counter = 0
vote_count = []
vote_perc = []

# Function to find unique items on a list
def unique(input_list):
    # Initialize an empty list
    list_unique = []
    # Populate it with unique elements
    for item in input_list:
        if item not in list_unique:
            list_unique.append(item)
    return list_unique

with open(path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")

    # Skip the header so it is omitted
    next(csv_reader)

    for row in csv_reader:
        # Count the total number of votes cast
        total_votes = total_votes + 1

        # Create a list with the candidates column
        candidates.append(row[2])

    # Obtain a complete list of the candidates who received votes
    unique_candidates = unique(candidates)

    # Count the votes for each candidate
    for name in unique_candidates:
        for vote in candidates:
            if name == vote:
                vote_counter = vote_counter + 1
        vote_count.append(0)
        vote_count[loop_num] = vote_counter
        loop_num = loop_num + 1
        vote_counter = 0
    
    # Calculate the percentage of votes for each candidate
    for num in vote_count:
        vote_perc.append(format(num / total_votes * 100, ".3f"))

    # Get the winner
    winner_votes = max(vote_count)
    winner_name = unique_candidates[vote_count.index(winner_votes)]

    # Print in terminal      
    print("")
    print("Election Results")
    print("------------------------------------")
    print("Total votes:", total_votes)
    print("------------------------------------")
    for i in range(len(unique_candidates)):
        print(f"{unique_candidates[i]}: {vote_perc[i]}% ({vote_count[i]})")
    print("------------------------------------")
    print(f"Winner: {winner_name}")
    print("------------------------------------")
    print("")

    # Open and read csv file
    write_path = os.path.join('.', 'Analysis', 'analysis.txt')
    with open(write_path, "w+") as output:
        output.write("Election Results\n")
        output.write("------------------------------------\n")
        output.write(f"Total votes:{total_votes}\n")
        output.write("------------------------------------\n")
        for i in range(len(unique_candidates)):
            output.write(f"{unique_candidates[i]}: {vote_perc[i]}% ({vote_count[i]})\n")
        output.write("------------------------------------\n")
        output.write(f"Winner: {winner_name}\n")
        output.write("------------------------------------\n")