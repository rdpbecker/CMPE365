import csv

##############################################################
## Finds the index of the minimum value in a list which is 
## greater than low
##
## Parameters: aList - the list to be checked
##             low - the lower threshold for the minimum value
##
## Returns: the index of the minimum value in the list which 
##          is greater than low
##          -1 if there is no element of the list greater than
##          low
##############################################################

def minG(aList,low):
   index = -1
   i = 0
   ## Find the first entry which is at least low
   while (i < len(aList)) and (aList[i] < low):
      i = i + 1
   ## If we didn't find one return it
   if i == len(aList):
      return index
   ## Index of first element which is at least low
   index = i
   min = aList[i]
   ## Now we'll go through the rest of them to find the
   ## minimum
   while i < len(aList):
      if (aList[i] >= low) and (aList[i] < min):
         index = i
         min = aList[i]
      i = i + 1
   return index
   
##############################################################
## Print the flights coming out of each gate nicely
##
## Parameters: gates - a list of lists for which the ith list
##                     is a list of the arrival and departure
##                     times for each flight using the ith 
##                     gate
##
## Returns: Nothing
##############################################################
   
def printGates(gates):
   for i in range(len(gates)):
      print "Gate ", i, ":\n"
      for j in range(len(gates[i])):
         print "Flight ", j, ":"
         print "   Arrives at:", gates[i][j][0]
         print "   Departs at:", gates[i][j][1]
      print "\n\n"
      
def writeGates(gates,writePath):
   with open(writePath,'wb') as writeFile:
      for i in range(len(gates)):
         writeFile.write("Gate "+str(i)+":\n")
         for j in range(len(gates[i])):
            writeFile.write("Flight "+str(gates[i][j][0])+":\n")
            writeFile.write("   Arrives at:"+str(gates[i][j][1])+"\n")
            writeFile.write("   Departs at:"+str(gates[i][j][2])+"\n")
         writeFile.write("\n\n")
      
##############################################################
## Reads a file
##
## Parameters: filepath - the filepath of the file to read
##
## Returns: a list with all the arrival or departure times 
##############################################################

def readFile(filepath):
   timesList = []
   with open(filepath,'rb') as csvfile:
      theReader = csv.reader(csvfile)
      for row in theReader:
         timesList.append(float(row[0]))
   return timesList
      
##############################################################
## Performs the scheduling algorithm
##
## Parameters: None
##
## Returns: the list of gates as formatted for the 
## printGates() function
##############################################################

def main():
   ## Read the file to get the start and end times
   filepathStart = "../Flight Lists/start1.csv"
   filepathFinish = "../Flight Lists/finish1.csv"
   startTimes = readFile(filepathStart) 
   finishTimes = readFile(filepathFinish)
#   startTimes = [2,3,4,14.5,8,10]
#   finishTimes = [3,5,14,16,15,13]
   n = len(startTimes)
   flightNums = range(n)
   num = 0
   gates = []
   ## While we haven't added everything to the gates list
   while num < n:
      ## This will be a list of flight for the current gate
      flightList = []
      maximum = max(finishTimes)
      finish = 0
      ## As long as there's another flight which arrives 
      ## after the current one leaves
      while minG(startTimes,finish) >= 0:
         ## Find index, and arrival (start) and departure
         ## (finish) times, and add the arrival and 
         ## departure times to the list for the current
         ## gate
         flight = minG(startTimes,finish)
         start = startTimes.pop(flight)
         finish = finishTimes.pop(flight)
         flightList.append((flightNums.pop(flight),start,finish))
      num = num + len(flightList)
      gates.append(flightList)
   
   writePath = "../Outputs/Test1_1_1.txt"
   writeGates(gates,writePath)
   return gates
      
def main2():
   ## Read the file to get the start and end times
   filepathStart = "../Flight Lists/start1.csv"
   filepathFinish = "../Flight Lists/finish1.csv"
   startTimes = readFile(filepathStart) 
   finishTimes = readFile(filepathFinish)
#   startTimes = [2,3,4,14.5,8,10]
#   finishTimes = [3,5,14,16,15,13]
   n = len(startTimes)
   num = 0
   gates = []
   numGates = 0
   for flight in range(n):
      gate = 0
      while gate < numGates:
         if startTimes[flight] > gates[gate][-1][2]:
            gates[gate].append((flight,startTimes[flight],finishTimes[flight]))
            break
         gate = gate + 1
      if gate == numGates:
         gates.append([(flight,startTimes[flight],finishTimes[flight])])
         numGates = numGates + 1
         
   writePath = "../Outputs/Test1_1_2.txt"
   writeGates(gates,writePath)
   return gates
      
list0 = [2,3,4,7,8,10]
main()