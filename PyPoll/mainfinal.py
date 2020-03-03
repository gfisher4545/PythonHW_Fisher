import os
import csv

resource_path = os.path.join('Resources','election_data.csv')
new_path = os.path.join('Resources','results.txt')

with open (resource_path) as csvfile:
    resource_data = csv.reader(csvfile, delimiter = "," )
    header = next(csvfile)
    #print (header)
    votes = []
    candidates = []
    khan = []
    correy = []
    li = []
    otooley = []
    winner = []
    for row in resource_data:
        votes.append(row[0])
        candidates.append(row[2])
        #print(row[2])
        
    total_votes = len(votes)
 vote_stas = {}
for name in candidates:
    if name not in vote_stas:
        vote_stas[name] =  1
    else:
        vote_stas[name] = vote_stas[name] + 1
vote_stas
max(vote_stas.values())
can_name = list(vote_stas.keys())
can_num = list(vote_stas.values())
can_name, can_num
max_num = max(can_num)
max_index = can_num.index(max_num)
can_name[max_index]
winner = can_name[max_index]
#print(winner)
khan_pct = round(can_num[0] / total_votes,5)*100
#print(khan_pct)
correy_pct = round(can_num[1] / total_votes,5)*100
li_pct = round(can_num[2] / total_votes,5)*100 
ot_pct = round(can_num[3] / total_votes,5)*100

results = (
f"Election Results\n"
f"-----------------------------\n"
f"Total Votes: {total_votes}\n"
f"-----------------------------\n"
f"Khan: {khan_pct}% ({can_num[0]})\n"
f"Correy: {correy_pct}% ({can_num[1]})\n"
f"Li: {li_pct}% ({can_num[2]})\n" 
f"O'Tooley: {ot_pct}% ({can_num[3]})\n"   
f"-----------------------------\n"
f"Winner: {winner}\n"
f"-----------------------------\n"
)
#print(results)
with open (new_path,'w') as txt_file:
    txt_file.write(results)