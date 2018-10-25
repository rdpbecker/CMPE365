##############################################################
## Finds all the maximal sets of indexes which occur in the 
## same list in a list of lists more than a threshold. The 
## list of lists should be located in 
## ../Test Data/testListTESTNUM.csv
##
## Parameters: threshold - the minimum number of times two
##                         indexes can occur in the same list
##                         which will be caught
##             testnum - the set of test value to be tested
##             flag - a flag which decides whether or not to 
##                    print the subsets
##
## Returns: nothing - the results are printed
##############################################################

def main(threshold,testnum,flag):
    ## Set up the filePath according to the command line arguments
    filepath = "../Test Data/testList"+str(testnum)+".csv"
    ## Read the file and print the resulting list of lists
    lists = io.readFile(filepath)
    printing.printLists(lists)
    ## Find the maximum value in the list of lists
    n = popG.findMax(lists)
    ## Initialize the graph
    graph = popG.initGraph(n)
    ## Populate the graph and print it
    popG.populateGraph(graph,lists,n)
    print "Final Graph:"
    printing.printGraph(graph)
    ## Find the graph of connections and print it
    connected = find.aboveThreshold(graph,threshold)
    print "The connections are"
    printing.printGraph(connected)
    ## From the graph of connections, find all the maximal 
    ## subsets of passengers who were on the same flight
    ## more than the threshold
    cycles = find.findCycles(connected,n,flag)

## Set up the command line arguments and import all the
## other modules in this directory
if __name__ == "__main__":
    import sys, fileio as io, populateGraph as popG, printing, findConnectedFlyers as find
    main(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]))
