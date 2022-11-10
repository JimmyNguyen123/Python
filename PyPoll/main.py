import os
import csv

# Python file and csv file stay in the same folder for ease of access
filepath=os.path.join('Resources','election_data.csv')

candidates_raw=[]
totalvotes=0
candidates_votes={}
candidatevotes=1

print("Election Results \n--------------")

#Open file and skip header
with open(filepath,'r') as file:
    filereader=csv.reader(file,delimiter=',')
    fileheader=next(filereader)

#Calculate total votes by increment and separate raw candidate names to a list    
    for row in filereader:
        totalvotes=totalvotes+1
        candidates_raw.append(row[2])
    
    print(f"Total Votes: {totalvotes:,}")
    print("--------------")

    #sort list 
    candidates_raw=sorted(candidates_raw)
    
    #add item (candidate name) as the key, if key is the same through loop then add 1 to value as number of votes ELSE add candidate names to dict and set value of key to 1
    for item in candidates_raw:
        if item in candidates_votes:
            candidates_votes[item]=candidates_votes[item]+1
        else:
            candidates_votes[item]=1
    
    for item in candidates_votes:
        print(f"{item}: {(candidates_votes[item]/totalvotes):.3%} ({candidates_votes[item]:,})")
    
    print("--------------")
#use max to go through dict but compare the value instead of key. result is dict key with highest value
    winner=max(candidates_votes,key=candidates_votes.get)
    print(f"Winner: {winner}")
    print("--------------")

resultpath=os.path.join('Analysis','result.txt')
with open(resultpath,'w') as result:
    
    result.write("Election Results \n---------\n")
    result.write("Total Votes: " + str("{:,}".format(totalvotes)))
    result.write( "\n---------")
    for item in candidates_votes:
        result.write("\n"+item +": "+str("{:.3%}".format(candidates_votes[item]/totalvotes))+ " ("+str("{:,}".format(candidates_votes[item]))+")")
    result.write( "\n---------\n")
    result.write("Winner: "+winner)
    result.write( "\n---------")
    
    