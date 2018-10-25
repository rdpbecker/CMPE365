import csv

##############################################################
## Read the (CSV) file at location filePath
##
## Parameters: filePath - the location of the file to be read.
##                        Should only contain integers
##
## Returns: a list of lists, where the ith list is the list 
##          of integers in the ith row of the CSV file
##############################################################

def readFile(filePath):
    ## The final list of lists
    lists = []
    with open(filePath,'r') as csvreader:
        reader = csv.reader(csvreader,delimiter = ' ')
        for row in reader:
            ## The initial list of strings for the next row
            list1 = row[0].split(',')
            ## An empty list to store the integers in
            list2 = []
            for thing in list1:
                ## Check to make sure we're not converting an
                ## empty string to an integer since CSVs are 
                ## stored in rectangular arrays
                if thing != '':
                    list2.append(int(thing))
            lists.append(list2)
    return lists
