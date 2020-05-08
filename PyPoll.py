import csv
import os

# Assign variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
# Create file to store analysis results
file_to_save = os.path.join('analysis','election_analysis.txt')

# Open the election results and read the file
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)

# with open(file_to_save,'w') as txt_file:
#     txt_file.write("Counties in the election\n--------------\nArapahoe\nDenver\nJefferson")
#      # To do: perform analysis.
#      print(election_data)
# # Close the file.
# election_data.close()
