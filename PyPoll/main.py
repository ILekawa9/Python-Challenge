import os

import csv

election_csv= os.path.join("Resources","election_data.csv")
output_file=os.path.join("analysis","election-analysis.txt")


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

print("Election Results")
print("---------------------")
print("Total Votes:"+ str(Total_Votes))
print("---------------------")
print(f"Khan: {Khan_percent} ({Khan_Votes})")
print(f"Li: {Li_percent} ({Li_Votes})")
print(f"Correy: {Correy_percent} ({Correy_Votes})")
print(f"O'Tooley: {Otooley_percent} ({Otooley_Votes})")
print("---------------------")
print("Winner:", Election_Winner)
print("---------------------")