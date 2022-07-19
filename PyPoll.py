import csv
import os

# Assign a variable for the file to load nad the path>
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize Votes couinter
total_votes = 0

# Candidate options
candidate_options = []

# Candidate Votes Dictionary
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:

     # To do: perform analysis.
     file_reader = csv.reader(election_data)
     #Print each row in csv file.
     headers = next(file_reader)
     #Print each row in csv file.
     for row in file_reader :
          #add total votes
          total_votes += 1
          #candidate names from each row :
          candidate_name = row[2]
          #If candidate is already in the list, don't add again
          if candidate_name not in candidate_options :
               candidate_options.append(candidate_name)

               #Track Candidate vote count:
               candidate_votes[candidate_name] = 0

          #Add votes to respective candidate
          candidate_votes[candidate_name] += 1
     for candidate_name in candidate_votes:
          votes = candidate_votes[candidate_name]
          vote_percentage = float(votes) / float(total_votes) * 100
          print (f"{candidate_name}: recieved {vote_percentage:.1f}% of the total votes ,({votes})")


          if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
               winning_count = votes
               winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
               winning_candidate = candidate_name
               winning_candidate_summary = (
               f"-------------------------\n"
               f"Winner: {winning_candidate}\n"
               f"Winning Vote Count: {winning_count:,}\n"
               f"Winning Percentage: {winning_percentage:.1f}%\n"
               f"-------------------------\n")
print(winning_candidate_summary)

     
