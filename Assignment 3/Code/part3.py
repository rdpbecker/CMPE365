import sys, random, matplotlib as plt

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

def generateUniform(n,a,b):
   points = []
   for i in range(n):
      points.append((random.uniform(a,b),random.uniform(a,b)))
   return points
   
##############################################################
## Generate a set of n points with both coordinates normally
## distributed with mean a and variance b
## 
## Parameters: n - the number of points required
##             a - the mean of the distibution
##             b - the variance of the distribution
##
## Returns - a list of n points (formatted as tuples)
##############################################################

def generateNormal(n,a,b):
   points = []
   for i in range(n):
      points.append((random.gauss(a,b),random.gauss(a,b)))
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
## Takes a set of points and finds its convex hull
##
## Parameters: points - the set of points
##
## Returns: The points on the hull
##############################################################

def jarvisMarch(points):
   ## Find the length of the points
   n = len(points)
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
   
   ## Return the set of points on the hull
   return hullPoints
   
##############################################################
## Extracts the x- and y-coordinates from a set of points
##
## Parameters: points - the list of points
##
## Returns: xCoords - a list of the x-coordinates
##          yCoords - a list of the y-coordinates
##############################################################
   
def extractCoords(points):
   xCoords = []
   yCoords = []
   for point in points:
      xCoords.append(point[0])
      yCoords.append(point[1])
   return xCoords,yCoords
   
##############################################################
## Find the average of the values in a list
##
## Parameters: aList - the list
##
## Returns: the average of the list
##############################################################

def avg(aList):
   return sum(aList)/len(aList)
   
##############################################################
## Finds the distance between two points in the plane
##
## Parameters: point1 - the first point
##             point2 - the second point
##
## Returns: the distance between point1 and point2
##############################################################
   
def dist(point1,point2):
   return ((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)**0.5
   
##############################################################
## Finds the maximum distance of a set of points from their
## center
## 
## Parameters: center - the center point
##             points - the set of points
##
## Returns: the maximum distance of the points from their 
##          center
##############################################################
   
def radius(center,points):
   maxRadius = 0
   for point in points:
      if dist(point,center) > maxRadius:
         maxRadius = dist(point,center)
   return maxRadius
   
##############################################################
## Check if the bounding circles for the convex hulls of two 
## uniformly generated sets of points overlap. Each set has 
## n points, with first set distributed between a1 and b1 
## and the second between a2 and b2
##
## Parameters: flag - 1 for uniform distributions, 0 for
##                    normal
##             n - the number of points in each set
##             a1, b1 - parameters for first distribution
##             a2, b2 - parameters for first distribution
##
## Returns: 1 if the bounding circles for the convex hulls 
##          overlap, 0 otherwise
##############################################################

def checkOverlap(flag,n,a1,b1,a2,b2):
   ## Generate the sets of points and find their hulls
   if flag:
      setA = generateUniform(n,a1,b1)
      setB = generateUniform(n,a2,b2)
   else:
      setA = generateNormal(n,a1,b1)
      setB = generateNormal(n,a2,b2)
   hullA = jarvisMarch(setA)
   hullB = jarvisMarch(setB)
   
   ## Do all the plotting
   setAx,setAy = extractCoords(setA)
   setBx,setBy = extractCoords(setB)
   hullAx,hullAy = extractCoords(hullA)
   hullBx,hullBy = extractCoords(hullB)
   plt.plot(setAx,setAy,'b.')
   plt.plot(setBx,setBy,'c.')
   plt.plot(hullAx,hullAy,'ro')
   plt.plot(hullBx,hullBy,'mo')
   
   ## Approximate the centers of the hulls
   centerA = (avg(hullAx),avg(hullAy))
   centerB = (avg(hullBx),avg(hullBy))
   ## Find the maximum radii of the hulls and add the bounding
   ## circles to the plot
   rA = radius(centerA,hullA)
   rB = radius(centerB,hullB)
   circleA = plt.Circle(centerA,rA,color='r',fill=False)
   circleB = plt.Circle(centerB,rB,color='m',fill=False)
   ax = plt.gca()
   ax.add_patch(circleA)
   ax.add_patch(circleB)
   plt.axis('scaled')
   plt.show()
   ## If the distance between the centers is less than the sum
   ## of the radii the circles overlap
   if rA+rB >= dist(centerA,centerB):
      return 1
   return 0

##############################################################
## Just do the import and the function call. No command line
## arguments here
##############################################################
if __name__ == "__main__":
   import sys, random, matplotlib.pyplot as plt
   args = sys.argv[1:]
   flag = int(args[0])
   n = int(args[1])
   a1 = int(args[2])
   b1 = int(args[3])
   a2 = int(args[4])
   b2 = int(args[5])
   print checkOverlap(flag,n,a1,b1,a2,b2)