##############################################################
## Find the maximum value in a list of lists
##
## Parameters: lists - a list of lists
##
## Returns: the maximum value in lists
##############################################################

def findMax(lists):
    maxVal = lists[0][-1]
    for i in range(1,len(lists)):
        if lists[i][-1] > maxVal:
            maxVal = lists[i][-1]
    return maxVal

##############################################################
## Converts a list of integers to a binary list, where 
## binaryList[index-1] is 1 if index is in the list and 0
## if not
##
## Parameters: aList - the original list to be checked
##             n - the maximum index that could be in aList
##
## Returns: a list of 1s and 0s, where 1 indicates that
##          index+1 is in aList and 0 indicates that it is not
##############################################################

def toBinary(aList,n):
    list1 = []
    count = 0
    length = len(aList)
    for i in range(n):
        if (count < length) and (aList[count] == (i+1)):
            list1.append(1)
            count = count + 1
        else:
            list1.append(0)
    return list1

##############################################################
## Adds two lists of the same length
##
## Parameters: list1 - the first list
##             list2 - the second list
##
## Returns: the sum of the two lists
##############################################################

def addLists(list1,list2):
    listSum = []
    for i in range(len(list1)):
        listSum.append(list1[i]+list2[i])
    return listSum

##############################################################
## Initialize a graph with no edges and vertices 1 through n
##
## Parameters: n - the value of the maximum vertex in the 
##                 graph
##
## Returns: a graph with vertices 1 through max(lists) and no
##          edges
##############################################################

def initGraph(n):
    graph = {}
    for i in range(n):
        graph[i+1] = [0]*n
    return graph

##############################################################
## Populates a graph with no edges, where the weight of the
## edge i->j is the number of times i and j are present in the
## same list
##
## Parameters: graph - a graph with no edges and vertices 1
##                     through n, implemented as a dictionary 
##                     with the set of vertices as the keys 
##                     and the values as lists containing the 
##                     weights of the edges between the key
##                     and every other vertex
##             lists - a list of lists for which the 
##                     copresence is to be tested
##             n - the maximum value in lists
##
## Returns: nothing - the graph is changed in place
##############################################################

def populateGraph(graph,lists,n):
    for aList in lists:
        list1 = toBinary(aList,n)
        for i in range(n):
            if list1[i] == 1:
                graph[i+1] = addLists(list1,graph[i+1])
