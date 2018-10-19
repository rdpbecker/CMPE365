import csv

def readFile(filePath):
    lists = []
    with open(filePath,'r') as csvreader:
        reader = csv.reader(csvreader,delimiter = ' ')
        for row in reader:
            list1 = row[0].split(',')
            list2 = []
            for thing in list1:
                if thing != '':
                    list2.append(int(thing))
            lists.append(list2)
    return lists

def printLists(lists):
    for aList in lists:
        print aList

if __name__ == "__main__":
    lists = readFile("../Test Data/testList2.csv")
    printLists(lists)
    num = popG.findMax(lists)
    for aList in lists:
        popG.toBinary(aList,num)
