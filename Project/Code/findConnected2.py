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
        nonzero = 0
        for node in range(maxVal):
            if graph[key][node] >= threshold:
                connected[key][node] = 1
                if node != key+1:
                    nonzero = 1
        if nonzero:
            connected[key].append(1)
        else:
            connected[key].append(0)

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

def binaryToList(aList,binList,length):
    newList = []
    for i in range(length):
        if binList[i]:
            newList.append(aList[i])
    return newList

##############################################################
## Finds all the subsets of {1,...,length} and returns them in 
## a list
##
## Parameters: length - the maximum value in the list
## 
## Returns: a set containing all the subsets of 
##          {1,...,length}
##############################################################

def subsets(aList,length):
    subsetList = []
    i = 2**length-1
    while i>=0:
        if not (2**length-1-i)%100:
            print 2**length-1-i
        subsetList.append(binaryToList(aList,numToBinary(i,length),length))
        i = i-1
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
    nonzeroNodes = []
    for vertex in connected.keys():
        if connected[vertex][-1]:
            nonzeroNodes.append(vertex)
    length = len(nonzeroNodes)
    print 2**length
    count = 0
    for subset in subsets(nonzeroNodes,len(nonzeroNodes)):
        count = count+1
        if not count%100:
            print count
        flag = 0
#        ## Check if the current subset is a subset of one of 
#        ## the cliques
#        for clique in cliques:
#            if isSubset(subset,clique):
#                flag = 1
#                ## Need to break out of this loop before we 
#                ## can continue
#                break
#        if flag:
#            continue
        ## For the subgraph in question, take its adjacency 
        ## matrix and determine from it whether the subgraph
        ## is complete
        for i in subset:
            for j in subset:
                if not connected[i][j-1]:
                    flag = 1
                    break
            if flag:
                break
        if flag:
            continue
        cliques.append(subset)
    cliques.pop(-1)
    return cliques

# if __name__ == "__main__":
#    import sys
 #   num = int(sys.argv[1])
#    length = int(sys.argv[2])
  #  print subsets(num)
