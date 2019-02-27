import csv
import os

pathcsv = os.path.join("C:\\Users\\silva\\Desktop\\LearnPython\\HomeworkSupport\\budget_data.csv")
 
maxinc = 0
maxdec = 0
mthcount = 0
nettotal = 0
value = 0
change = 0
mon = []
var = []

with open(pathcsv, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")


    csvheader = next(csvreader)

    
    firstline = next(csvreader)
    mthcount += 1
    nettotal += int(firstline[1])
    pnl = int(firstline[1])
    

    for row in csvreader:

        mon.append(row[0])
        

        change = int(row[1])-pnl
        var.append(change)
        pnl = int(row[1])
        mthcount += 1
        nettotal = nettotal + int(row[1])


    maxinc = max(var)
    maxloc = var.index(maxinc)
    maxincd = mon[maxloc]


    mininc = min(var)
    minloc = var.index(mininc)
    minincd = mon[minloc]


    avgchg = sum(var)/len(var)




l1 = "Financial Analysis"
l2 = "---------------------"
l3 = str(f"Total Months: {str(mthcount)}")
l4 = str(f"Total: ${str(nettotal)}")
l5 = str(f"Average Change: ${str(round(avgchg,2))}")
l6 = str(f"Greatest Increase in Profits: {maxincd} (${str(maxinc)})")
l7 = str(f"Greatest Decrease in Profits: {minincd} (${str(mininc)})")

print(l1)
print(l2)
print(l3)
print(l4)
print(l5)
print(l6)
print(l7)


file = open("C:\\Users\\silva\\Desktop\\LearnPython\\HomeworkSupport\\budget_data2.csv",'w')
file.write(l1+'\n')
file.write(l2+'\n')
file.write(l3+'\n')
file.write(l4+'\n')
file.write(l5+'\n')
file.write(l6+'\n')
file.write(l7)

file.close()

#Financial Analysis
#----------------------------
#Total Months: 86
#Total: $38382578
#Average  Change: $-2315.12
#Greatest Increase in Profits: Feb-2012 ($1926159)
#Greatest Decrease in Profits: Sep-2013 ($-2196167)
