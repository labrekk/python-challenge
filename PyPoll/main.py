#FROM README
#   * The total number of votes cast

#   * A complete list of candidates who received votes

#   * The percentage of votes each candidate won

#   * The total number of votes each candidate won

#   * The winner of the election based on popular vote.


#import os and csv to python
import os
import csv

#path for csv
poll_csv = os.path.join('.', 'resources', 'election_data.csv')

#open the csv
#https://docs.python.org/3/library/csv.html




with open(poll_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    total_votes = 0
    voter_id = [0]
    county = [1]
    candidate = [2]
    voteskhan = 0
    votescorrey = 0
    votesli = 0
    votesotooley = 0
    percentkhan = 0
    percentli = 0
    percentcorrey = 0
    percentotooley = 0



    #skipping the header row of the csv
    csv_header = next(csvfile)

#loop rows of election csv... logic is, "if the name = x, then add x+1"
    for row in csvreader:
        
        total_votes = total_votes + 1

        if row[2] == 'Khan':
            voteskhan = voteskhan + 1
        elif row[2] == 'Correy':
            votescorrey = votescorrey + 1
        elif row[2] == 'Li':
            votesli = votesli + 1
        elif row[2] == "O'Tooley":
            votesotooley = votesotooley + 1

        #Percentages
        percentkhan = (voteskhan / total_votes)*100
        percentcorrey = (votescorrey / total_votes)*100
        percentli = (votesli / total_votes)*100
        percentotooley = (votesotooley/total_votes)*100
    
    winner = max(voteskhan, votescorrey, votesli, votesotooley)

#       Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------

    print ("Election Analysis")
    print ("----------------------------")
    print (f"Total Votes: {total_votes}")
    print (f"Khan: {percentkhan} ({voteskhan})")
    print (f"Correy: {percentcorrey} ({votescorrey})")
    print (f"Li: {percentli} ({votesli})")
    print (f"O'Tooley: {percentotooley} ({votesotooley})")
    print(f"Winner: {winner}")
            
#https://www.guru99.com/reading-and-writing-files-in-python.html
f = open("Election_analysis.txt", "w+")

#Source for \n bits:
#https://www.freecodecamp.org/news/python-new-line-and-how-to-python-print-without-a-newline/#:~:text=The%20new%20line%20character%20in%20Python%20is%20%5Cn%20.,used%20to%20separate%20the%20lines.
f.write ("Election Analysis\n")
f.write ("----------------------------\n")
f.write (f"Total Votes: {total_votes}\n")
f.write (f"Khan: {percentkhan} ({voteskhan})\n")
f.write (f"Correy: {percentcorrey} ({votescorrey})\n")
f.write (f"Li: {percentli} ({votesli})\n")
f.write (f"O'Tooley: {percentotooley} ({votesotooley})\n")
f.write ("----------------------------\n")
f.write (f"Winner: {winner}\n")

f.close()   




