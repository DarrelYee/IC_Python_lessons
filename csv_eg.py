# Import the csv module
import csv

# Open the csv file
with open('BC.csv', 'r+', newline = '') as file:
    # Read each row in the csv
    fileRead = csv.DictReader(file)
    for row in fileRead:
        print (row)


with open('names.csv', 'a+', newline = '') as file:
    # Write a row to the csv
    fileWrite = csv.writer(file)
    fileWrite.writerow(['4','2', '9', '40'])

    
    
