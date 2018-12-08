import os
import csv

csvpath = os.path.join("budget_data.csv")

TotalMonths = []
Total = []

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    
    for row in csvreader:
        #Add each month to list TotalMonths
        TotalMonths.append(row[0])
        
        #Add each Profit/Loss to list Total as an integer
        Total.append(int(row[1]))              
        
    #sums the valves in the list
    net = sum(Total)

    #Average change using Total / TotalMonths
    Diff = [Total[i+1]-Total[i] for i in range(len(Total)-1)]
    AvgDifSum = sum(Diff)
    AvgDif = round(AvgDifSum / len(Diff),2)
    
    #Finding the Greatest Increase in Profits and the month-year
    GreatInc = max(Diff)
    TotalMonths[Diff.index(GreatInc)+1]
        
    #Finding the Greatest Decrease in Profits and the month-year
    GreatDec = min(Diff)
    TotalMonths[Diff.index(GreatDec)+1]

    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(len(TotalMonths)))
    print("Total: $" + str(net))
    print("Average Change: $" + str(AvgDif))
    print("Greatest Increase in Profits: " + TotalMonths[Diff.index(GreatInc)+1]  + " (" + str(GreatInc) + ")")
    print("Greatest Decrease in Profits: " + TotalMonths[Diff.index(GreatDec)+1] + " (" + str(GreatDec) + ")")
    
    budget = open("budget_data.txt","w+")
    budget.write("Financial Analysis")
    budget.write("\n")
    budget.write("----------------------------")
    budget.write("\n")
    budget.write("Total Months: " + str(len(TotalMonths)))
    budget.write("\n")
    budget.write("Total: $" + str(net))
    budget.write("\n")
    budget.write("Average Change: $" + str(AvgDif))
    budget.write("\n")
    budget.write("Greatest Increase in Profits: " + TotalMonths[Diff.index(GreatInc)+1] + " (" + str(GreatInc) + ")")
    budget.write("\n")
    budget.write("Greatest Decrease in Profits: " + TotalMonths[Diff.index(GreatDec)+1] + " (" + str(GreatDec) + ")")
    budget.close()