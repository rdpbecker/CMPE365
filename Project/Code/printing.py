##############################################################
## Prints a list of lists
##
## Parameters: lists - the list of lists to be printed
## 
## Returns: nothing
##############################################################

def printLists(lists):
    for aList in lists:
        print aList

##############################################################
## Prints a graph
##
## Parameters: graph - the graph to be printed
## 
## Returns: nothing
##############################################################

def printGraph(graph):
    for key in graph.keys():
        print key, ': ', graph[key]
