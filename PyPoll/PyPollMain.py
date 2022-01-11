import os

import csv

election_csv= os.path.join("Resources","election_data.csv")
file_to_output=os.path.join("Analysis","election-analysis.txt")


Khan = []
Correy = []
Li = []
OTooley = []


with open(election_csv) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')


    for row in csvreader:
        if row[2] == "Khan":
            Khan.append(1)
        
        if row[2] == "Correy":
            Correy.append(1)

        if row[2] == "Li":
            Li.append(1)
        
        if row[2] == "O'Tooley":
            OTooley.append(1)
       
    
Total_Votes= int(len(Khan)+len(Correy)+len(Li)+len(OTooley))

Khan_Votes = int(len(Khan))
Khan_percent = "{:.3%}".format(Khan_Votes/Total_Votes)

Correy_Votes = int(len(Correy))
Correy_percent = "{:.3%}".format(Correy_Votes/Total_Votes)

Li_Votes = int(len(Li))
Li_percent = "{:.3%}".format(Li_Votes/Total_Votes)

Otooley_Votes = int(len(OTooley))
Otooley_percent = "{:.3%}".format(Otooley_Votes/Total_Votes)    

Candidate_votes = [Khan_Votes, Correy_Votes, Li_Votes, Otooley_Votes]
Highest_votes = max(Candidate_votes)
Election_Winner = " "
if Khan_Votes > Correy_Votes and Khan_Votes > Li_Votes and Khan_Votes > Otooley_Votes:
    Election_Winner = "Khan"
elif Li_Votes > Correy_Votes and Li_Votes > Khan_Votes and Li_Votes > Otooley_Votes:
    Election_Winner = "Li"
elif Correy_Votes > Khan_Votes and Correy_Votes > Li_Votes and Correy_Votes > Otooley_Votes:
    Election_Winner = "Correy"
elif Otooley_Votes > Correy_Votes and Otooley_Votes > Li_Votes and Otooley_Votes > Khan_Votes:
    Election_Winner = "O'Tooley"
else:
    Election_Winner = "Nobody"


output = (
    f"Election Results\n"
    f"---------------------\n"
    f"Total Votes: {str(Total_Votes)}\n"
    f"---------------------\n"
    f"Khan: {Khan_percent} ({Khan_Votes})\n"
    f"Li: {Li_percent} ({Li_Votes})\n"
    f"Correy: {Correy_percent} ({Correy_Votes})\n"
    f"O'Tooley: {Otooley_percent} ({Otooley_Votes})\n"
    f"---------------------\n"
    f"Winner: {Election_Winner}\n"
    f"---------------------\n")

print(output)

with open(file_to_output, "w") as txt_file:
    txt_file.write(output)