# The with keyword is used when creating a context manager 
# i.e managing the context of the ongoing operation (in this case a file open operation)

""" 
The mode is an optional parameter. It’s a string that specifies the 
mode in which you want to open the file. The following table shows 
available modes for opening a text file:

'r'	Open for text file for reading text
'w'	Open a text file for writing. If the file exists, the function will truncate all the contents as soon as you open it. If the file doesn’t exist, the function creates a new file.
'a'	Open a text file for appending text. If the file exists, the function append contents at the end of the file.
‘+’	Open a text file for updating (both reading & writing).
"""

# writing to a file
lines = ['My name is Trust', 'I am a software engineer', 'Learning to become a data scientist']
with open('write.txt', 'w') as f:
    for line in lines:
        # write the line to the file
        f.write(line)
        f.write('\n')
        # You can check the write.md to see the result

