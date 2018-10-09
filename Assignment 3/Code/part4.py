##############################################################
## Check if pointA and pointB are on the same side of the 
## line between point1 and point2
## 
## Parameters: point1 - the first point to check for the 
##                      potential dividing line
##             point2 - the second point to check for the 
##                      potential dividing line
##             pointA - the point on hull A
##             pointB - the point on hull B
##
## Returns: 1 if pointA and pointB are on opposite sides of 
##          the line between point1 and point2, 0 otherwise
##############################################################

def opposite(point1,point2,pointA,pointB):
   if part3.left(point1,point2,pointA) == part3.left(point1,point2,pointB):
#      print point1,point2,pointA,pointB," Not opposite"
      return 0
#   print point1,point2,pointA,pointB," Opposite"
   return 1

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
      setA = part3.generateUniform(n,a1,b1)
      setB = part3.generateUniform(n,a2,b2)
   else:
      setA = part3.generateNormal(n,a1,b1)
      setB = part3.generateNormal(n,a2,b2)
   hullA = part3.jarvisMarch(setA)
   hullB = part3.jarvisMarch(setB)
   nA = len(hullA)
   nB = len(hullB)
   
   ## Do all the plotting
   setAx,setAy = part3.extractCoords(setA)
   setBx,setBy = part3.extractCoords(setB)
   hullAx,hullAy = part3.extractCoords(hullA)
   hullBx,hullBy = part3.extractCoords(hullB)
   plt.plot(setAx,setAy,'b.')
   plt.plot(setBx,setBy,'c.')
   plt.plot(hullAx,hullAy,'ro')
   plt.plot(hullBx,hullBy,'mo')
   plt.show()
   
   ## Do the check. We'll only choose all the lines that go
   ## along the outside of the hull (so that all the other 
   ## points on that hull are on the same side as the line),
   ## and if there is a point from the other hull on the same
   ## side of the line as all the points from the hull the 
   ## line comes from, the line is not a dividing line
   
   for i in range(nA):
      point1 = hullA[i]
      point2 = hullA[(i+1)%nA]
      pointA = hullA[(i+2)%nA]
      flag = True
      for pointB in hullB:
         if not opposite(point1,point2,pointA,pointB):
            flag = False
            break
      if flag: 
         return 0
         
   for i in range(nB):
      point1 = hullB[i]
      point2 = hullB[(i+1)%nB]
      pointB = hullB[(i+2)%nB]
      flag = True
      for pointA in hullA:
         if not opposite(point1,point2,pointA,pointB):
            flag = False
            break
      if flag:
         return 0
   return 1

if __name__ == "__main__":
   import sys, matplotlib.pyplot as plt, part3
   args = sys.argv[1:]
   flag = int(args[0])
   n = int(args[1])
   a1 = int(args[2])
   b1 = int(args[3])
   a2 = int(args[4])
   b2 = int(args[5])
   print checkOverlap(flag,n,a1,b1,a2,b2)