import sys

def read_dataset(file_name):
    #First open the file for reading. 
    data_file = open(file_name, 'r')

    #Will hold dataset. 
    dataset = []

    #Each line is a separate datapoint. 
    for line in data_file: 
        dataset.append(read_line(line))

def read_line(line): 
    #First separate all data fields. 
    data = line.split()[7:]

    #Now return tuple of 
