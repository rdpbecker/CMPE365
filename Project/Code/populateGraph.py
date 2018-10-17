def findMax(lists):
    maxVal = lists[0][-1]
    for i in range(1,len(lists)):
        if lists[i][-1] > maxVal:
            maxVal = lists[i][-1]
    return maxVal

def toBinary(aList,n):
    list1 = []
    count = 0
    for i in range(n):
        if aList[count] == (i+1):
            list1[i] = 1
            count = count + 1
        else:
            list1[i] = 0
    return list1

def addLists(list1,list2):
    listSum = []
    for i in range(len(list1)):
        listSum.append(list1[i]+list2[i])
    return listSum

def initGraph(lists):
    maxVal = findMax(lists)
    graph = {}
    for i in range(maxVal):
        graph[i] = [0]*maxVal
    return graph

def populateGraph(graph,lists):
    for aList in lists:
        list1 = toBinary(aList,maxVal)
        for i in range(maxVal):
            if list1[i] == 1:
                graph[i] = addLists(list1,graph[i])
