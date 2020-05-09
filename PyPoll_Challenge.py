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
counties_list=[]
counties_votes={}
county_turnout=""
county_count=0
county_percentage=0


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

        #Add county name to list
        countie_name=row[1]
        #IF county is not on list, add
        if countie_name not in counties_list:
            #Add county name to list
            counties_list.append(countie_name)
            #Tracking county vote count
            counties_votes[countie_name]=0
        #Add a vote to each county count
        counties_votes[countie_name]+=1

# Open the election results and read the file.   
with open(file_to_save,'w') as txt_file:
    # Print the final vote count to the terminal.
    election_results=(
        f"Election Results\n"
        f"--------------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"--------------------------------\n"
        f"\n"
        f"County Votes:\n")
    print(election_results, end="")
    #Save the final vote count to the text file
    txt_file.write(election_results)
    
    #Determine the total number of vote per county
    for county in counties_votes:
        #Retriece county vote count
        cvotes=counties_votes[county]
        #Calculate percentage of total election votes
        cvote_percentage=float(cvotes)/float(total_votes)*100
        #Print the result per county
        county_result=(
            f"{county}: {cvote_percentage:.1f}% ({cvotes:,})\n")
        print(county_result)
        #Write to analysis file
        txt_file.write(county_result)
        #Determine the county turnout
        if (cvotes>county_count) and (cvote_percentage>county_percentage):
            county_count=cvotes
            county_percentage=cvote_percentage
            county_turnout=county
    #Print county with highest turnout
    county_turnout_summary=(
        f"\n"
        f"-------------------------\n"
        f"Largest County Turnout: {county_turnout}\n"
        f"-------------------------\n")
    print(county_turnout_summary)
    #writte to analysis file
    txt_file.write(county_turnout_summary)
    
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