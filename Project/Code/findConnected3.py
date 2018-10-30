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


