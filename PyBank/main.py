import os
import csv

month=0
amount=0
profit_loss=[]
change =[]
totalchange=0
month_date=[]
max_increase=0
min_decrease=0
max_position=0
min_position=0

# Python file and csv file stay in the same folder for ease of access
filepath=os.path.join("Resources","budget_data.csv")

with open(filepath,'r') as datafile:
    datafilereader=csv.reader(datafile,delimiter=",")
    datafileheader=next(datafilereader)
 
# Calculate totalmonths and total by incrementing values  
    for row in datafilereader:
        month=month+1
        amount=amount+int(row[1])
        profit_loss.append(int(row[1]))
        month_date.append(row[0])

# Profit/Loss is the result of change from next row to last. Following loop means to put all change in 1 list then calculate Average  
    for i in range(1,len(profit_loss)):
        change.append(profit_loss[i]-profit_loss[i-1])   
    avg_change=sum(change)/len(change)

# Find the max/min change in change list by setting initial value then compare value through list. If element higher than initial value then update, ELSE stay the same 
# max/min's position is 1 index less to row's. From min/max position, month posision will be max/min position +1 
    for a in range(len(change)):
        if change[a]>max_increase:
            max_increase=change[a]
            max_position=a
        else:
            max_increase=max_increase
            max_position=max_position
    
    for a in range(len(change)):
        if change[a]<min_decrease:
            min_decrease=change[a]
            min_position=a
        else:
            min_decrease=min_decrease
            min_position=min_position   

# Print all results to command prompt   
    print("Financial Analysis \n -----------------------------------------------------")
    print(f"Total Months: {month}")
    print(f"Total: $ {amount:,}")
    print(f"Average Change: ${avg_change:,.2f}")
    print(f"Greatest increase in Profits: {month_date[max_position+1]} (${max_increase:,})")
    print(f"Greatest decrease in Profits: {month_date[min_position+1]} (${min_decrease:,})")

# Write result to txt file
resultpath=os.path.join("Analysis","result.txt")
with open(resultpath,'w') as result:
    result.write("Financial Analysis \n ----------------------------------------------------- \n")
    result.write("Total Months: " + str(month))
    result.write("\nTotal: $"+str("{:,}".format(amount)))
    result.write("\nAverage Change: $" + str("{:.2f}".format(avg_change)))
    result.write("\nGreatest increase in Profits: " + str(month_date[max_position+1])+" ($"+str("{:,}".format(max_increase))+")")
    result.write("\nGreatest decrease in Profits: " + str(month_date[min_position+1])+" ($"+str("{:,}".format(min_decrease))+")")