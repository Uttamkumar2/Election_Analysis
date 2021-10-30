#Add our dependencies 
import os
# Module for reading CSV files
import csv

#Assign a variable to load file from a path
file_to_load = os.path.join('Resources', 'election_results.csv')

#Assign a variable to save the output file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Open the election result and read the file.
print(file_to_load)
with open(file_to_load) as election_data:
    # to do : read and analyze the data here
    #Read the file object with the reader function
    file_reader = csv.reader(election_data)

    #Print the header row
    headers = next(file_reader)
    print(headers)

    #Print each row in the CSV file.
    #for row in file_reader:
    #    print(row)
