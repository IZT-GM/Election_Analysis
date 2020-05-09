import csv
import os

# Assign variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
# Create file to store analysis results
file_to_save = os.path.join('analysis','election_analysis.txt')

#Initialize variables
total_votes=0
candidate_options=[]
candidate_votes={}
winning_candidate=""
winning_count=0
winning_percentage=0

# Open the election results and read the file
with open(file_to_load) as election_data:
    
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    
    #Print each row in the csv file
    for row in file_reader:
        #Add to the total vote count
        total_votes += 1
        #Print candidate name
        candidate_name=row[2]
        #iF the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            #Add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            #Begin tracking that candidate's vote count
            candidate_votes[candidate_name]=0
        #Add a vote to that candidate's count
        candidate_votes[candidate_name]+=1

with open(file_to_save,'w') as txt_file:
    # Print the final vote count to the terminal.
    election_results=(
        f"Election Results\n"
        f"--------------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"--------------------------------\n")
    print(election_results, end="")
    #Save the final vote count to the text file
    txt_file.write(election_results)
    #Determine the percentage of votes for each candidate by looping though the counts
    for candidate in candidate_votes:
        #Retrieve vote count
        votes=candidate_votes[candidate]
        #Calculate percentage
        vote_percentage=float(votes)/float(total_votes)*100
        #Print the result percandidate
        candidate_results=(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        #Print candidate data
        print(candidate_results)
        #Write to file
        txt_file.write(candidate_results)
        #Determine winning vote count and candidate
        if (votes>winning_count) and (vote_percentage>winning_percentage):
            winning_count=votes
            winning_percentage=vote_percentage
            winning_candidate=candidate
    #Print winner
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    #Save winner results to file
    txt_file.write(winning_candidate_summary)
# print(f"The election winner is {winning_candidate} with {winning_count} votes and {winning_percentage:.1f}%")



#Print total votes
# print(total_votes)
#Print candidate list
# print(candidate_votes)

# with open(file_to_save,'w') as txt_file:
#     txt_file.write("Counties in the election\n--------------\nArapahoe\nDenver\nJefferson")
#      # To do: perform analysis.
#      print(election_data)
# # Close the file.
# election_data.close()
