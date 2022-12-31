import csv  

header = ['country', 'area code', 'city', 'state']
data = ['Nigeria', 200211, 'AGB', 'OG']

with open('writefile.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    
    # write the header
    writer.writerow(header)
    
    # write the data
    writer.writerow(data)