# Election-Analysis

## Overview of Election Audit
A Colorado board of election employees has given me the task to complete the election of audit of a recent local congressional election.
Analysis was done with following criteria in mind:
1. Calculate the number of votes cast.
2. Get a complete list of candidates who recieved votes.
3. Obtain a definitive list of all counties involved.
4. Calculate the total number of votes each candidate recieved.
5. Determine the total votes per county.
5. Calculate the percentage of votes each candidate won.
6. Determine the winner based on popular count vote.

## Election-Audit Results:
The analysis concluded the following outcomes:
- How many votes were cast in this congressional election?
  - There were 369,711 Total Votes.
- Breakdown of the number of votes and the percentage of total votes for each county in the precinct.
  - Denver: number of total votes 306,055 and that represented 82.8% of the total votes
  - Jefferson: number of total votes 38,855 and that represented 10.5% of the total votes
  - Arapahoe: number of total votes 24,801 and that represented 6.7% of the total votes
  - 
![Election_resilt_summary](https://github.com/A-Mossa/Election-Analysis/blob/main/County_votes_results.png)

- Which county had the largest number of votes?
  - Denver was the county with the largest number of votes (306,055)
- The Candidate results were:
  - Charles Casper Stockham: recieved 23.0% of the total votes ,(85213)
  - Diana DeGette: recieved 73.8% of the total votes ,(272892)
  - Raymon Anthony Doane: recieved 3.1% of the total votes ,(11606)
- The winner of the election was:
  - Diana DeGette, who recieved 73.8% of the total votes (272892)

## Election-Audit Summary
The code utilized this audit is sufficient to carry out the same analysis of results to almost any similar situation with minor tweaks.
given the next project posses a similar database, the code can be slightly refactored to accomodate difference and changes if the desired outcome is of the same nature as this audit.

![Code_screenshot](https://github.com/A-Mossa/Election-Analysis/blob/main/PyPollCode.png)

For example, if in the future should the stake holders wish to include additional attributes, then more variables would be created and code would be slightly modified to govern the interaction between said variables.
