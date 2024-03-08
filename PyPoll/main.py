import csv
import os

#Initialize variables
Total_votes = 0
list_of_candidates = []
list_of_votes = [0, 0, 0]
percentage_list = [0, 0, 0]
winner = ""

#Import the file
Election_csv = os.path.join("Resources", "election_data.csv")

#Read in the file
with open (Election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter= ",")

    #Read in header
    csv_header = next(csv_file)

     #Take in the data and analyze
    for line in csv_reader:
        Total_votes +=1
        if line[2] not in list_of_candidates:
            list_of_candidates.append(line[2])
        if line[2] == "Charles Casper Stockham":
            list_of_votes[0]+=1
        elif line[2] == "Diana DeGette":
            list_of_votes[1] +=1
        elif line[2 == "Raymon Anthony Doane"]:
            list_of_votes[2] +=1
    #Transform into percentage
    for i in range(3):
        percentage_list[i] = round(list_of_votes[i]/Total_votes*100, 3)
    #Find the winner
    winner = list_of_candidates[percentage_list.index(max(percentage_list))]

    #Print Results
    print(f"Election Results")
    print(f"Total Votes: {Total_votes}")
    for i in range(3):
        print(f"{list_of_candidates[i]}: {percentage_list[i]}% {list_of_votes[i]}")
    print(f"Winner: {winner}")

#Write the output
analysis = os.path.join("analysis", "Analysis.txt")
with open (analysis, 'w') as file:
    file.write(f"Election Results")
    file.write(f"\nTotal Votes: {Total_votes}")
    for i in range(3):
        file.write(f"\n{list_of_candidates[i]}: {percentage_list[i]}% {list_of_votes[i]}")
    file.write(f"\nWinner: {winner}")