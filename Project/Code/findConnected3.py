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
        connected[key] = list2
    return connected

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

def setIntersect(set1,set2):
    inBoth = {}
    newSet = []
    for thing in set1:
        inBoth[thing] = 1
    for thing in set2:
        if thing in inBoth.keys():
            newSet.append(thing)
    return newSet

def findCliques(connected,vertices,remaining):
    if not remaining:
        print vertices
    while remaining:
        vertex = remaining[0]
    #    print vertices, remaining
        findCliques(connected,setUnion(vertices,vertex),setIntersect(remaining,connected[vertex]))
        remaining.pop(0)

if __name__ == "__main__":
    import sys
    num = len(sys.argv)-1
    list1 = []
    list2 = []
    breakIndex = int(sys.argv[num])
    for i in range(1,breakIndex+1):
        list1.append(int(sys.argv[i]))
    for i in range(breakIndex+1,num):
        list2.append(int(sys.argv[i]))
    print list1
    print list2
    print setIntersect(list1,list2)
