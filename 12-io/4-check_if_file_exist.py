import os.path

"""
We can check if a file exist before proceeding 
to make any computational operation with the file
"""

file_exists = os.path.exists('ellajoyifeoma.txt')

if(file_exists):
    print("File exists")
else:
    print("File does not exist")