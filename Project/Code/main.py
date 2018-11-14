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
    if flag:
        print "Using 3:\n"
        connected = find3.aboveThreshold(graph,threshold,n)
#        print "The connections are"
        printing.printGraph(connected)
        ## From the graph of connections, find all the maximal 
        ## subsets of passengers who were on the same flight
        ## more than the threshold
        cliques = []
        print "The cliques are:\n"
        find3.findCliques(cliques,connected,[],connected.keys(),connected.keys())
        printing.printLists(cliques)
        ## For every clique, find all the subsets of that clique,
        ## indexed by number, and add them to a list
        allSubsetsList = []
        for clique in cliques:
            allSubsetsList.extend(setops.subsetsByIndex(clique,n))
        ## To avoid duplicates, add every one of the subsets to a 
        ## dictionary. The list of keys is implemented as a hash 
        ## table so it's fast to look up key values, and if we add
        ## a key twice it still only exists once in the key list
        allSubsetsDict = {}
        for subset in allSubsetsList:
            allSubsetsDict[subset] = 1
        ## Finally, for each of the indexes in the dictionary, 
        ## convert them back to sets
        print "All the subsets are:\n"
        uniqueSubsetKeys = sorted(allSubsetsDict.keys())
        uniqueSubsetKeys.reverse()
        uniqueSubsetKeys.pop(-1)
        uniqueSubsets = []
        for num in uniqueSubsetKeys:
            uniqueSubsets.append(setops.numToSet(num,n))

        printing.printLists(uniqueSubsets)
        return uniqueSubsets
    else:
        print "Using 2:\n"
        connected = popG.initGraph(n)
        find2.aboveThreshold(graph,connected,threshold,n)
        print "The graph of connections"
        printing.printGraph(connected)
        cliques = find2.findCliques(connected,n)
        print "All the connected groups are"
        printing.printLists(cliques)

## Set up the command line arguments and import all the
## other modules in this directory
if __name__ == "__main__":
    import sys, fileio as io, populateGraph as popG, printing, findConnected2 as find2, findConnected3 as find3, setOperations as setops
    threshold = int(sys.argv[1])
    testnum = int(sys.argv[2])
    flag = int(sys.argv[3])
#    if flag:
#        times = 0
#        for i in range(5):
#            times = times + main(threshold,testnum,flag)
#        print times/5
#    else:
#        printing.printLists(main(threshold,testnum,flag))
    main(threshold,testnum,flag)
