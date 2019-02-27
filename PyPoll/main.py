import csv
import os

pathcsv = os.path.join("C:\\Users\\silva\\Desktop\\LearnPython\\HomeworkSupport\\election_data.csv")
 
cands = []
votes = []
voteper = []
votettl = 0
#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.

with open(pathcsv, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader:
        votettl += 1 
        if row[2] not in cands:
            cands.append(row[2])
            index = cands.index(row[2])
            votes.append(1)
        else:
            index = cands.index(row[2])
            votes[index] += 1
    
    for v in votes:
        percentage = (v/votettl) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        voteper.append(percentage)
    
  
    winning = max(votes)
    index = votes.index(winning)
    winner = cands[index]




l1 = "Election Results"
l2 = "-------------------------"
l3 = str(f"Total Votes: {str(votettl)}")
l4 =  "-------------------------"
l6 =  "-------------------------"
l7 = str(f"Winner: {winner}")
l8 =  "-------------------------"

print(l1)
print(l2)
print(l3)
print(l4)
for i in range(len(cands)):
    print(f"{cands[i]}: {str(voteper[i])} ({str(votes[i])})")
print(l6)
print(l7)
print(l8)


file = open("C:\\Users\\silva\\Desktop\\LearnPython\\HomeworkSupport\\electiondata2.csv",'w')
file.write(l1+'\n')
file.write(l2+'\n')
file.write(l3+'\n')
file.write(l4+'\n')
for i in range(len(cands)):
    line = str(f"{cands[i]}: {str(voteper[i])} ({str(votes[i])})")
    file.write('{}\n'.format(line))  
file.write(l6+'\n')
file.write(l7+'\n')
file.write(l8+'\n')
file.close()


#  Election Results
#  -------------------------
#  Total Votes: 3521001
#  -------------------------
#  Khan: 63.000% (2218231)
#  Correy: 20.000% (704200)
#  Li: 14.000% (492940)
#  O'Tooley: 3.000% (105630)
#  -------------------------
#  Winner: Khan
#  -------------------------
