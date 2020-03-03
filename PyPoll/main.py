import os
import csv

resource_path = os.path.join('Resources','election_data.csv')
new_path = os.path.join('Resources','results.txt')

with open (resource_path) as csvfile:
    resource_data = csv.reader(csvfile, delimiter = "," )
    header = next(csvfile)
    print (header)


