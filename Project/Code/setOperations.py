##############################################################
## Perform a set union of a set and a single element
##
## Parameters: vertices - the set
##             new - the single element
##
## Returns: the union of the new element with the set, as a 
##          deep copy
##############################################################

def setUnion(vertices,new):
    flag = 1
    newSet = []
    for vertex in vertices:
        if vertex == new:
            flag = 0
        newSet.append(vertex)
    if flag:
        newSet.append(new)
    return newSet

##############################################################
## Finds the intersection of 2 sets
##
## Parameters: set1 - the first set
##             set2 - the second set
##
## Returns: the intersection of set1 and set2
##############################################################

def setIntersect(set1,set2):
    inBoth = {}
    newSet = []
    for thing in set1:
        inBoth[thing] = 1
    for thing in set2:
        if thing in inBoth.keys():
            newSet.append(thing)
    return newSet

##############################################################
## Finds the difference between two sets
## 
## Parameters: set1 - the first set
##             set2 - the second set
##
## Returns: the difference between set1 and set2
##############################################################

def setSubtract(set1,set2):
    count1 = 0
    count2 = 0
    setSub = []
    while count1 < len(set1) and count2 < len(set2):
        if set1[count1] == set2[count2]:
            count2 = count2 + 1
        else:
            setSub.append(set1[count1])
        count1 = count1 + 1
    while count1 < len(set1):
        setSub.append(set1[count1])
        count1 = count1 + 1
    return setSub

##############################################################
## Converts a number to a binary string with a specified
## length
## 
## Parameters: n - the number to be converted
##             length - the length of the output string
##
## Returns: a binary representation of n with the specified
##          length, as a list
##############################################################

def numToBinary(n,length):
    aList = []
    for i in range(length-1,-1,-1):
        k = n/(2**i)
        aList.append(k)
        n = n - k*(2**i)
    return aList

##############################################################
## Given a binary list and another list of the same length, 
## creates a list containing aList[i] if and only if 
## binList[i] is 1. Used in subsetsByIndex
## 
## Parameters: aList - the list for which a subset is to be 
##                     found
##             binList - a list of 1s and 0s
##             length - the length of the two lists
##
## Returns: a subset of aList given by the binary list
##############################################################

def binaryToList(aList,binList,length):
    endList = []
    for i in range(length):
        if binList[i]:
            endList.append(aList[i])
    return endList

##############################################################
## Converts a list of positive integers a number whose binary 
## representation is d_{maxVal-1}...d_0 where d_i is 1 if and
## only if maxVal-i is in the list
##
## Parameters: aList - the list to convert
##             maxVal - the maximum allowable value in the 
##                      list. Used to index the complete 
##                      subgraphs in the overall graph and
##                      ensure uniqueness
##
## Returns: the number which represents the list
##############################################################

def listToNum(aList,maxVal):
    num = 0
    for n in aList:
        num = num + 2**(maxVal-n)
    return num

##############################################################
## Converts a number to a set by converting it to its binary
## representation d_{maxVal-1}...d_0 and including the i if 
## and only if d_{maxVal-i} is 1. The inverse of listToNum as
## long as maxVal is the same
##
## Parameters: num - the number to be converted
##             maxVal - the maximum possible value in the list
##
## Returns: the set represented by num
##############################################################

def numToSet(num,maxVal):
    aSet = []
    for i in range(1,maxVal+1):
        k = num/(2**(maxVal-i))
        if k:
            aSet.append(i)
        num = num - k*(2**(maxVal-i))
    return aSet

##############################################################
## Finds all the subsets of a list with a specified maximum 
## value
##
## Parameters: aList - the list for which the subsets are to 
##                     be found
##             maxVal - the maximum possible value in the list
##
## Returns: a list of indexes representing all the subsets of
##          aList. The binary representation of each index is 
##          the one given by listToNum
##############################################################

def subsetsByIndex(aList,maxVal):
    length = len(aList)
    subsetList = []
    for i in range(2**length-1,-1,-1):
        ## Take the numeric representation of each subset of
        ## aList, converts it to its binary representation,
        ## converts that binary representation to the list 
        ## represented by it, then converts that list to the
        ## index the set would have if it was a subset of
        ## {1,...,maxVal}
        subsetList.append(listToNum(binaryToList(aList,numToBinary(i,length),length),maxVal))
    return subsetList

if __name__ == "__main__":
    import sys
    length = int(sys.argv[-1])+1
    list1 = []
    list2 = []
    for i in range(1,length):
        list1.append(int(sys.argv[i]))
    for i in range(length,len(sys.argv)-1):
        list2.append(int(sys.argv[i]))
    print list1,list2
    print setSubtract(list1,list2)
