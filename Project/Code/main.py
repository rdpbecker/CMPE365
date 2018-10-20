def main(threshold,testnum,flag):
    filepath = "../Test Data/testList"+str(testnum)+".csv"
    lists = io.readFile(filepath)
    printing.printLists(lists)
    graph = popG.initGraph(lists)
    popG.populateGraph(graph,lists)
    print "Final Graph:"
    printing.printGraph(graph)
    connected = find.aboveThreshold(graph,threshold)
    print "The connections are"
    printing.printGraph(connected)
    cycles = find.findCycles(connected,popG.findMax(lists),flag)

if __name__ == "__main__":
    import sys, fileio as io, populateGraph as popG, printing, findConnectedFlyers as find
    main(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[2]))
