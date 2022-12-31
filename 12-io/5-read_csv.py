import csv

with open('readfile.csv', 'r') as f:
    csv_reader = csv.reader(f)
    for line in csv_reader:
        # process each line
        print(f'{line}\n')