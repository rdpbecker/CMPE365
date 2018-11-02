##############################################################
## Given a graph with vertices 1 to maxVal and another empty 
## graph with the same vertices, fills in the empty graph so 
## that i->j is 1 if i->j is greater than the threshold in the 
## original graph and 0 otherwise
##
## Parameters: graph - the original (weighted) graph as a 
##                     dictionary
##             connected - an empty graph with the same
##                         vertices as graph
##             threshold - the threshold for the weights in
##                         graph
##             maxVal - the value of the maximum node in graph
##
## Returns: Nothing. The result is stored in connected
##############################################################

def aboveThreshold(graph,connected,threshold,maxVal):
    for key in graph.keys():
        for node in range(maxVal):
            if graph[key][node] >= threshold:
                connected[key][node] = 1

##############################################################
## Converts a number to binary
##
## Parameters: n - the number to be converted
##             length - the length of the output binary string
##
## Returns: the binary representation of n as a list
##############################################################

def numToBinary(n,length):
    aList = []
    for i in range(length-1,-1,-1):
        k = n/(2**i)
        aList.append(k)
        n = n - k*(2**i)
    return aList

##############################################################
## Convert a binary list to a regular list
## 
## Parameters: binList - a list containing only 1s and 0s
##             length - the length of the binary list
##
## Returns: a list containing k if and only if binList[k]=1
##############################################################

def binaryToList(binList,length):
    aList = []
    for i in range(length):
        if binList[i]:
            aList.append(i+1)
    return aList

##############################################################
## Finds all the subsets of {1,...,length} and returns them in 
## a list
##
## Parameters: length - the maximum value in the list
## 
## Returns: a set containing all the subsets of 
##          {1,...,length}
##############################################################

def subsets(length):
    subsetList = []
    for i in range(2**length-1,-1,-1):
        subsetList.append(binaryToList(numToBinary(i,length),length))
    return subsetList

##############################################################
## Determines whether list1 is a subset of list2, where list1
## and list2 are sorted lists
##
## Parameters: list1 - the potential subset
##             list2 - the potential superset
##
## Returns: 1 if list1 is a subset of list2
##          0 if list1 is not a subset of list2
##############################################################

def isSubset(list1,list2):
    n1 = len(list1)
    n2 = len(list2)
    count1 = 0
    count2 = 0
    ## As long as we're not at the end of either list, check
    ## if the next element in list1 is equal to the next
    ## element in list2. If it is, move to the next element 
    ## in list1, and move to the next element in list2 either
    ## way
    while (count1<n1) and (count2<n2):
        if list1[count1] == list2[count2]:
            count1 = count1 + 1
        count2 = count2 + 1
    ## If we've reached the end of list1, it is either a 
    ## subset of list2 or is equal to list2. Since we only
    ## care about strict subsets, make sure list1 is actually
    ## shorter than list2
    if (count1 == n1) and (n1 < n2):
        return 1
    return 0
    return subsetList

##############################################################
## Finds all the cliques in a graph called connected
##
## Parameters: connected - an unweighted graph implemented as
##                         a dictionary
##             maxVal - the maximum value of the vertices in 
##                      connected
##
## Returns: a set of all the cliques in connected
##############################################################

def findCliques(connected,maxVal):
    cliques = []
    for subset in subsets(maxVal):
        flag = 0
        for clique in cliques:
            if isSubset(subset,clique):
                flag = 1
                break
        if flag:
            continue
        for i in subset:
            for j in subset:
                if not connected[i][j-1]:
                    flag = 1
                    break
            if flag:
                break
        if flag:
            continue
        cliques.insert(0,subset)

# if __name__ == "__main__":
#    import sys
 #   num = int(sys.argv[1])
#    length = int(sys.argv[2])
  #  print subsets(num)
