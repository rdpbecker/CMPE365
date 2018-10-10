import random, csv

##############################################################
## Add random lateness to arrival and departure times in place
##
## Parameters: startList - the list of arrival times
##             finishList - the list of departure times
##             lateMax - a limit on how late planes can be
##             split1 - the approximate percentage of late
##                      arrivals
##             split2 - the approximate percentage of late
##                      departures
##
## Returns: the percentage of flights that arrived and 
##          departed late, respectively (as decimals)
##############################################################

def randomify(startList,finishList,lateMax,split1,split2):
   startLate = 0
   finishLate = 0
   for i in range(len(startList)):
      ## Decide whether or not this flight will arrive late
      ## with probability split1
      if random.uniform(0,1) < split1:
         startList[i] = startList[i] + random.uniform(0,lateMax)
         startLate = startLate + 1
      ## Decide whether or not this flight will depart late
      ## with probability split2
      if random.uniform(0,1) < split2:
         finishList[i] = finishList[i] + random.uniform(0,lateMax)
         finishLate = finishLate + 1
      ## Allow for 15 mins between arrival and departure
      if startList[i] > finishList[i] - 0.25:
         startList[i] = finishList[i] - 0.25
   return float(startLate)/len(startList), float(finishLate)/len(finishList)

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
      print "Gate ", i+1, ":\n"
      for j in range(len(gates[i])):
         print "Flight ", j+1, ":"
         print "   Arrives at:", gates[i][j][0]
         print "   Departs at:", gates[i][j][1]
      print "\n\n"
      
##############################################################
## Writes the gates to a file using the same formatting as 
## printGates()
##
## Parameters: startLate - the percentage of flights that 
##                         arrive late, as a decimal
##             finishLate - the percentage of flights that 
##                          depart late, as a decimal
##             gates - a list of lists containing the flights
##                     directed towards each gate
##             writePath - the path of the (.txt) file to 
##                         be written to
##
## Returns: Nothing
##############################################################
      
def writeGates(startLate,finishLate,gates,writePath):
   with open(writePath,'wb') as writeFile:
      writeFile.write(str(startLate*100)+"% of flights arrived late\n")
      writeFile.write(str(finishLate*100)+"% of flights departed late\n")
      for i in range(len(gates)):
         writeFile.write("Gate "+str(i+1)+":\n")
         for j in range(len(gates[i])):
            writeFile.write("Flight "+str(gates[i][j][0]+1)+":\n")
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
##          printGates() function, and the percentages of 
##          flights that arrived and departed late
##############################################################

def main():
   ## Read the file to get the start and end times
   filepathStart = "../Flight Lists/start1.csv"
   filepathFinish = "../Flight Lists/finish1.csv"
   startTimes = readFile(filepathStart) 
   finishTimes = readFile(filepathFinish)
#   startTimes = [2,3,4,14.5,8,10]
#   finishTimes = [3,5,14,16,15,13]
   lateMax = 0.5
   startLate, finishLate = randomify(startTimes,finishTimes,lateMax)
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
   
   writePath = '../Outputs/Test2_1_0.5.txt'
   writeGates(startLate,finishLate,gates,writePath)
   return gates, startLate, finishLate
      
sum = 0
m = 1000
for i in range(m):
   gates, start, end = main()
   sum = sum + len(gates)
print float(sum)/m