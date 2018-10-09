##############################################################
## Generate a set of n points with both coordinates uniformly
## distributed between a and b
## 
## Parameters: n - the number of points required
##             a - the bottom of the coordinate range
##             b - the top of the coordinate range
##
## Returns - a list of n points (formatted as tuples)
##############################################################

def generatePoints(n,a,b):
   points = []
   for i in range(n):
      points.append((random.uniform(a,b),random.uniform(a,b)))
   return points

##############################################################
## Find the point in a list with the minimum y-coordinate
## 
## Parameters: points - the list of points
##             n - the number of points in the list
##
## Returns - the point with the minimum y-coordinate
##############################################################
   
def minY(points,n):
   minPoint = points[0]
   minY = points[0][1]
   for i in range(n):
      if points[i][1] < minY:
         minPoint = points[i]
         minY = points[i][1]
   return minPoint
   
##############################################################
## Determines whether a number is negative
##
## Parameters: num - the number to be checked
##
## Returns: 1 if num is positive
##          -1 if num is negative
##          0 if num is 0
##############################################################

def isNeg(num):
   if num > 0:
      return 1
   if num == 0:
      return 0
   return -1

##############################################################
## Determines if a point is left of the line between start 
## and end
##
## Parameters: point - the point to be checked
##             start - the start point of the line
##             end - the end point of the line
##
## Returns: 1 if point is on the left
##          0 if point is on the right
##
## Note: No support for colinear points, but the probability 
##       of colinear points in this context is 0
##############################################################
 
def left(point,start,end):
   ## Find the slope of the line from start to end
   m1 = slope(start,end)
   ## Find the slope of the line from start to point
   m2 = slope(start,point)
   
   ## Check if end and point are on the same side of start, 
   ## since the check is different. If they're on the same 
   ## side, we want the slope from start to point to be 
   ## bigger, otherwise we want it to be smaller
   if isNeg(point[0]-start[0]) == isNeg(end[0]-start[0]):
      if (m2 > m1):
         return 1
   else:
      if m2 < m1:
         return 1
   return 0
   
##############################################################
## Finds the slope of the line between two points
## 
## Parameters: point1 - the first point on the line
##             point2 - the seccond point on the line
##
## Returns: the slope if the line is not vertical
##          100000000 if the line is vertical
##############################################################

def slope(point1,point2):
   if point1[0] != point2[0]:
      return (point1[1]-point2[1])/(point1[0]-point2[0])
   return 100000000

##############################################################
## Plots the set of points in blue and its convex hull in red
##
## Parameters: points - the set of points
##             hullPoints - the hull of the set of points
##
## Returns: Nothing
##############################################################

def plotBoth(points,hullPoints):
   xcoords = []
   ycoords = []
   hullx = []
   hully = []
   
   ## Need to split the x and y coordinates for the plot
   ## function
   for point in points:
      xcoords.append(point[0])
      ycoords.append(point[1])
   for point in hullPoints:
      hullx.append(point[0])
      hully.append(point[1])
      
   ## Plot the points and print them
   plt.plot(xcoords,ycoords,'b.')
   plt.plot(hullx,hully,'ro')
   plt.show()

##############################################################
## Generates a set of points and finds its convex hull
##
## Parameters: n - the number of points to generate
##             a - the bottom of the coordinate range
##             b - the top of the coordinate range
##             flag - 0 for a single run, 1 otherwise
##
## Returns: The percentage of points on the hull
##############################################################
   
def jarvisMarch(n,a,b,flag):
   ## Generate the points
   points = generatePoints(n,a,b)
   ## Start at the lowest point
   currentHullPoint = minY(points,n)
   ## Array for the points on the hull
   hullPoints = []
   ## Not really necessary but it gives the number of hull
   ## points at the end
   i = 0
   while True:
      ## Append the current hull point
      hullPoints.append(currentHullPoint)
      ## Set the new end point to the first point in the list
      endpoint = points[0]
      ## For each point in the list, if it's the current 
      ## start point skip it, if not we'll check whether it's 
      ## on the left side of the line between the current 
      ## hull start point and the current end point. If it is
      ## replace the end point with the current point
      for j in range(1,n):
         if points[j] == currentHullPoint:
            continue
         if left(points[j],currentHullPoint,endpoint):
            endpoint = points[j]
      i = i + 1
      ## Set the current start point to the most recent end
      ## point. If the end point is the first point on the 
      ## hull (i.e. the lowest point) break out of the loop
      currentHullPoint = endpoint
      if (endpoint == hullPoints[0]):
         break
         
   ## If we're only doing one iteration plot it, if we're
   ## doing more skip this step cause it stops the program 
   ## every time
   if not flag:
      plotBoth(points,hullPoints)
      
   ## Return the percentage of points on the hull
   return i*100/float(n)

##############################################################
## Finds the convex hull of multiple points of set with a
## uniform distribution
##
## Parameters: numLoops - the number of sets of points to 
##                        generate
##             n - the number of points to generate in each 
##                 set
##             a - the bottom of the coordinate range
##             b - the top of the coordinate range
##             flag - 1, but it needs to be passed to 
##                    jarvisMarch
##
## Returns: Nothing
##############################################################

def main(numLoops,n,a,b,flag):
   percents = []
   for i in range(numLoops):
      percents.append(jarvisMarch(n,a,b,flag))
   print "The average percentage of points on the hull is: ", sum(percents)/numLoops

##############################################################
## For the script, import sys to read command line arguments
## and random for generating the uniform distribution. Only 
## import matplotlib if necessary cause it takes a long time
## to import
##
## Command Line Arguments:
##    1. flag - 0 for single run, 1 for loop
##    2. n - the number of points to generate in each set
##    3. a - the bottom of the coordinate range
##    4. b - the top of the coordinate range
##    5. numLoops - the number of loops to run in main(). Only
##                  necessary if looping
##############################################################   
if __name__ == "__main__":
   import sys, random
   args = sys.argv[1:]
   flag = int(args[0])
   n = int(args[1])
   a = int(args[2])
   b = int(args[3])
   if not flag:
      import matplotlib.pyplot as plt
      print jarvisMarch(n,a,b,flag)
   else:
      numLoops = int(args[4])
      main(numLoops,n,a,b,flag)