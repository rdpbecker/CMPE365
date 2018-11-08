import setOperations as setops

##############################################################
## Given a weighted graph G1, creates an unweighted graph G2 
## with the same vertices where the edge G2(i->j) exists if 
## the edge G1(i->j) has weight greater than the threshold.
## No edge is connected to itself in the output
##
## Parameters: graph - the original weighted graph
##             threshold - the threshold above which the
##                         vertices in the new graph are
##                         connected
##
## Returns: the new unweighted graph with vertices and edges
##          as given above
##############################################################

def aboveThreshold(graph,threshold,maxVal):
    connected = {}
    for key in graph.keys():
        list1 = graph[key]
        list2 = []
        ## If the number of times key and i occur in the same
        ## list is greater than or equal to the threshold,
        ## create an edge key->i
        for i in range(maxVal):
            if list1[i] >= threshold and (key != i+1):
                list2.append(i+1)
        if list2:
            connected[key] = list2
    return connected

##############################################################
## Find all the cliques in connected using a recursive method.
## The logic is explained in the lab report
## 
## Parameters: maximalList - a list to store all the cliques
##             connected - the graph in which to find the 
##                         cliques
##             vertices - the vertices already in the clique 
##                        being constructed 
##             remaining - a list of all the vertices 
##                         connected to every vertex in 
##                         vertices
##             excluded - the set of vertices which are not 
##                        allowed to be in the clique being
##                        constructed
##
## Returns: nothing. The list of cliques is stored in 
##          maximalList
##############################################################

def findCliques(maximalList,connected,vertices,remaining,excluded):
    if not excluded:
#        print vertices
        maximalList.append(vertices)
        return
    minVertex = excluded[0]
    maxlen = 0
    for vertex in excluded:
        if len(setops.setSubtract(remaining,connected[vertex])) > maxlen:
            maxlen = len(setops.setSubtract(remaining,connected[vertex]))
            minVertex = vertex
    newSet = setops.setSubtract(remaining,connected[minVertex])
    while newSet:
        vertex = newSet[0]
        findCliques(maximalList,connected,setops.setUnion(vertices,vertex),setops.setIntersect(remaining,connected[vertex]),setops.setIntersect(excluded,connected[vertex]))
        remaining.remove(vertex)
        newSet = setops.setSubtract(remaining,connected[minVertex])
