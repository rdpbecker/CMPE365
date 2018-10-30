def aboveThreshold(graph,connected,threshold,maxVal):
    for key in graph.keys():
        for node in range(maxVal):
            if graph[key][node] >= threshold:
                connected[key][node] = 1

def numToBinary(n,length):
    aList = []
    for i in range(length-1,-1,-1):
        k = n/(2**i)
        aList.append(k)
        n = n - k*(2**i)
    return aList

def binaryToList(binList,length):
    aList = []
    for i in range(length):
        if binList[i]:
            aList.append(i+1)
    return aList

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
