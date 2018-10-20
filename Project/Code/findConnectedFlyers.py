import printing

def aboveThreshold(graph,threshold):
    connected = {}
    maxVal = len(graph[1])
    for key in graph.keys():
        if graph[key][key-1] < threshold:
            connected[key] = [key]
            continue
        list1 = graph[key]
        list2 = []
        for i in range(maxVal):
            if list1[i] >= threshold:
                list2.append(i+1)
        connected[key] = list2
    return connected

def isSubset(list1,list2):
    n1 = len(list1)
    n2 = len(list2)
    count1 = 0
    count2 = 0
    while (count1<n1) and (count2<n2):
        if list1[count1] == list2[count2]:
            count1 = count1 + 1
        count2 = count2 + 1
    if (count1 == n1) and (n1 < n2):
        return 1
    return 0

def findCycles(connected,maxVal,flag):
    cycles = []
    inCycles = [0]*maxVal
    cycle = 1 
    for key in connected.keys():
        print inCycles, "\n"
        if not inCycles[key-1]:
            if not flag and (connected[key][0] == connected[key][-1]):
                print "After node ", key, ": "
                printing.printLists(cycles)
                continue
            for node in connected[key]:
                inCycles[node-1] = cycle
            cycle = cycle + 1
            cycles.append(connected[key])
        if inCycles[key - 1]:
            k = inCycles[key - 1] - 1
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
        print "After node ", key, ": "
        printing.printLists(cycles)
    return cycles
