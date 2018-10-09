import random

##############################################################
## Add random lateness to arrival and departure times in place
##
## Parameters: startList - the list of arrival times
##             finishList - the list of departure times
##             lateMax - a limit on how late planes can be
##
## Returns: Nothing
##############################################################

def randomify(startList,finishList,lateMax):
   ## Choose pproximates fractions of the arrivals and 
   ## departures to be late
   split1 = random.uniform(0,1)
   split2 = random.uniform(0,1)
   for i in range(len(startList)):
      ## Decide whether or not this flight will arrive late
      ## with probability split1
      if random.uniform(0,1) < split1:
         startList[i] = startList[i] + random.uniform(0,lateMax)
      ## Decide whether or not this flight will depart late
      ## with probability split2
      if random.uniform(0,1) < split2:
         finishList[i] = finishList[i] + random.uniform(0,lateMax)
      ## Allow for 15 mins between arrival and departure
      if startList[i] > finishList[i] - 0.25:
         startList[i] = finishList[i] - 0.25 

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
## Performs the scheduling algorithm
##
## Parameters: None
##
## Returns: the list of gates as formatted for the 
## printGates() function
##############################################################

def main():
   ## Read the file to get the start and end times
#   filepath = 
#   startTimes, finishTimes = readFile()
   startTimes = [2,3,4,14.5,8,10]
   finishTimes = [3,5,14,16,15,13]
   lateMax = 0.5
   randomify(startTimes,finishTimes,lateMax)
   n = len(startTimes)
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
         flightList.append((start,finish))
      num = num + len(flightList)
      gates.append(flightList)
   
   printGates(gates)
   return gates
      
list0 = [2,3,4,7,8,10]
main()