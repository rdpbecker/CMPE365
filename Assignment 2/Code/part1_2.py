import math

# Helper function 1

# Takes all the possible lists in the middle of the array
# and determines which one has the highest sum. Returns
# the start and end indices of the list with the highest
# sum
def findMax(leftMid,rightMid,midCross,leftRight,rightLeft):
   lists = [leftMid,rightMid,midCross,leftRight,rightLeft]
   max = leftMid[2]
   maxLength = leftMid[1] - leftMid[0]
   maxIndex = 0
   for i in range(1,5):
      if lists[i][2] > max or (lists[i][2] == max and (lists[i][1] - lists[i][0]) < maxLength):
         max = lists[i][2]
         maxLength = lists[i][1] - lists[i][0]
         maxIndex = i
   return lists[maxIndex]
   
# Helper function 3

# This is a variation on the first helper function for the ending 
# where we only have three arguments. Takes the three final output 
# 'lists' and finds the one with the largest sum
def findMax2(left,mid,right):
   lists = [left,mid,right]
   max = left[2]
   maxLength = left[1] - left[0]
   maxIndex = 0
   for i in [1,2]:
      if lists[i][2] > max or (lists[i][2] == max and (lists[i][1] - lists[i][0]) < maxLength):
         max = lists[i][2]
         maxLength = lists[i][1] - lists[i][0]
         maxIndex = i
   return lists[maxIndex]
   
# The main function

# The recursive function doing the dividing and conquering (and
# recreating)
def mss(aList,start,end):
   if end - start == 1:
      return [start,end,aList[start]], [start,end,aList[start]], [start,end,aList[start]]
      
   else:
      n = end - start
      midpoint = int(math.floor((start+end)/2))
      leftLeft, leftMid, leftRight = mss(aList,start,midpoint)
      rightLeft, rightMid, rightRight = mss(aList,midpoint,end)
      left = [leftLeft[0],leftLeft[1],leftLeft[2]]
      right = [rightRight[0],rightRight[1],rightRight[2]]
      if leftLeft[1] == midpoint and rightLeft[2] > 0:
         left[1] = rightLeft[1]
         left[2] = left[2] + rightLeft[2]
      if rightRight[0] == midpoint and leftRight[2] > 0:
         right[0] = leftRight[0]
         right[2] = right[2] + leftRight[2]
      midCross = [leftRight[0],rightLeft[1],leftRight[2]+rightLeft[2]]
      mid = findMax(leftMid,rightMid,midCross,leftRight,rightLeft)
      
      return left, mid, right
      
def realmss(aList,left,right):
   left, mid, right = mss(aList,left,right)
   print left, mid, right
   return findMax2(left,mid,right)