def main(threshold):
    filepath = "../Test Data/testList1.csv"
    lists = io.readFile(filepath)
    io.printLists(lists)
    graph = popG.initGraph(lists)
    printing.printGraph(graph)
    popG.populateGraph(graph,lists)
    print "Final Graph:"
    printing.printGraph(graph)
    connected = find.aboveThreshold(graph,threshold)
    print "The connections are"
    printing.printGraph(connected)
    cycles = find.findCycles(connected,popG.findMax(lists))
    printing.printLists(cycles)

if __name__ == "__main__":
    import sys, fileio as io, populateGraph as popG, printing, findConnectedFlyers as find
    main(int(sys.argv[1]))
