def aboveThreshold(graph,threshold):
    connected = {}
    maxVal = len(graph[1])
    for key in graph.keys():
        if graph[key][key-1] < threshold:
            connected[key] = []
            continue
        list1 = graph[key]
        list2 = []
        for i in range(maxVal):
            if list1[i] >= threshold:
                list2.append(i+1)
        connected[key] = list2
    return connected

def findCycles(connected,maxVal):
    cycles = []
    inCycles = [0]*maxVal
    for key in connected.keys():
        if (not inCycles[key-1]) and len(connected[key]):
            for node in connected[key]:
                inCycles[node-1] = 1
            cycles.append(connected[key])
    return cycles
