import printing

##############################################################
## Given a weighted graph G1, creates an unweighted graph G2 
## with the same vertices where the edge G2(i->j) exists if 
## the edge G1(i->j) has weight greater than the threshold
##
## Parameters: graph - the original weighted graph
##             threshold - the threshold above which the
##                         vertices in the new graph are
##                         connected
##
## Returns: the new unweighted graph with vertices and edges
##          as given above
##############################################################

def aboveThreshold(graph,threshold):
    connected = {}
    ## This is the maximum value in the graph
    maxVal = len(graph[1])
    for key in graph.keys():
        ## If a graph[key][key-1] < threshold, the key 
        ## doesn't occur in threshold number of lists,
        ## so there are certainly no connections.
        ## Indicate this by saying that key is connected
        ## to itself
        if graph[key][key-1] < threshold:
            connected[key] = [key]
            continue
        list1 = graph[key]
        list2 = []
        ## If the number of times key and i occur in the same
        ## list is greater than or equal to the threshold,
        ## create an edge key->i
        for i in range(maxVal):
            if list1[i] >= threshold:
                list2.append(i+1)
        connected[key] = list2
    return connected

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

##############################################################
## Given unweighted graph, find all the maximal complete
## subgraphs
##
## Parameters: connected - the unweighted graph
##             maxVal - the maximum possible value in the 
##                      graph
##             flag - a flag to print out the unconnected
##                    vertices
##
## Returns: the list of all maximal complete subgraphs of
##          connected

def findCycles(connected,maxVal,flag):
    cycles = []
    ## Dynamic programming YAY!!!!!!!
    inCycles = [0]*maxVal
    ## Set the current cycle number to 1 so inCycles[key]=0
    ## only if the key really isn't in a cycle
    cycle = 1
    ## Loop through each vertex in the graph
    for key in connected.keys():
        print inCycles, "\n"
        ## If it's not already in a subset, add the list of
        ## vertices connected to the vertex, set 
        ## inCycles[node] to the current cycle number, and 
        ## increment the new cycle number because we've added 
        ## a new one
        if not inCycles[key-1]:
            if not flag and (connected[key][0] == connected[key][-1]):
                print "After node ", key, ": "
                printing.printLists(cycles)
                continue
            for node in connected[key]:
                inCycles[node-1] = cycle
            cycle = cycle + 1
            cycles.append(connected[key])
        ## If the vertex is already in a subgraph S1, we want 
        ## to see if S1 a smaller subgraph S2 containing only
        ## nodes reached by the vertex because if we do, S1
        ## is not complete. If the set of nodes connected to 
        ## the vertex S3 is a subset of S1, we replace S1 with
        ## S3 to pare down the subgraphs that are not complete
        ## to subgraphs that are complete
        if inCycles[key - 1]:
            ## The most recent cycle that the current vertex 
            ## is in
            k = inCycles[key - 1] - 1
            ## If the set of nodes reached by this vertex S is
            ## a subset of cycles[k], it represents a 
            ## subgraph of the graph with V = cycles[k],
            ## so we replace cycles[k] with S. When we do this, 
            ## we need to update inCycles and set the nodes
            ## which are now excluded to 0
            if isSubset(connected[key],cycles[k]):
                count = 0
                aList = connected[key]
                n = len(aList)
                for node in cycles[k]:
                    if (count < n) and (aList[count] == node):
                        count = count + 1
                    else:
                        inCycles[node-1] = 0
                cycles[k] = connected[key]
        ## After we pass each node, print out the list of
        ## current maximal subgraphs
        print "After node ", key, ": "
        printing.printLists(cycles)
    return cycles
