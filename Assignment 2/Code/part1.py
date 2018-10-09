import math, copy # import the floor and deepcopy functions

# Helper function 1

# Finds the sum of the elements in a list
def sum(aList):
   sum = 0
   for i in aList:
      sum = sum + i
   return sum

# Helper function 2
   
# Takes all the possible lists in the middle of the array
# and determines which one has the highest sum. Returns a 
# deep copy of the list with the highest sum
def findMax(leftMid,rightMid,midCross,leftRight,rightLeft):
   lists = [rightMid,midCross,leftRight,rightLeft]
   max = sum(leftMid)
   maxList = leftMid # Don't care about deep copying yet
   for i in range(4):
      # Set this list as the max under one of 2 conditions:
         # 1. This list has the largest sum
         # 2. This list has a sum equal to the largest and is shorter than all other preceding lists with the same some
      if sum(lists[i]) > max or (sum(lists[i]) == max and len(lists[i]) < len(maxList)): 
         max = sum(lists[i])
         maxList = lists[i]
   return copy.deepcopy(maxList) # Now we return a deep copy

# Helper function 3

# This is just for the very end once we've found the largest sum in 
# the middle and starting from the left and right. Takes in the three 
# longest lists in those categories and determines the longest one. 
# Same function as before, just with 3 arguments instead of 5. 
# Returns a deep copy.
def findMax2(left,mid,right):
   lists = [mid,right]
   max = sum(left)
   maxList = left
   for i in range(2):
      if sum(lists[i]) > max:
         max = sum(lists[i])
         maxList = lists[i]
   return copy.deepcopy(maxList)

# The main function

# The recursive function doing the dividing and conquering (and 
# recreating)
def mss(aList):
   # If there's only one thing in the list just return the whole list 
   # as the left, middle, and right arrays with the highest sums
   if len(aList) == 1: 
      return aList, aList, aList
   # If there is more than one thing in the list, we'll have to 
   # divide and conquer
   else:
      # Just so we have it
      n = len(aList) 
      # Calculate the index of the middle of the list
      midpoint = int(math.floor(len(aList)/2)) 
      # Divide and conquer
      leftLeft, leftMid, leftRight = mss(aList[:midpoint])
      rightLeft, rightMid, rightRight = mss(aList[midpoint:])
      # Set the left subarray
      left = copy.deepcopy(leftLeft)
      # Set the right subarray
      right = copy.deepcopy(rightRight)
      # If the left subarray from the left half reaches all the way 
      # to the middle of the array, we should add the left subarray 
      # from the right half to the overall left subarray
      if len(leftLeft) == midpoint and sum(rightLeft) > 0:
         left.extend(rightLeft)
      # Same idea as above - if the right subarray from the right 
      # half reaches all the way to the middle, extend it
      if len(rightRight) == n - midpoint and sum(leftRight) > 0:
         right = leftRight + right
      # Combine the right subarray from the left half and the left 
      # subarray from the right half to create an array that spans 
      # across the middle of the overall array
      midCross = copy.deepcopy(leftRight)
      midCross.extend(rightLeft)
      # Determine which of all the possible subarrays from the 
      # interior of the overall array has the largest sum
      mid = findMax(leftMid,rightMid,midCross,leftRight,rightLeft)
      # Now that we've successfully combined everything, pass it back 
      # to the function that called it
      return left, mid, right

# Helper function 4 

# Calls mss on the overall array and then determines which of the 
# three resulting subarrays has the greatest sum. Returns the 
# subarray with the greatest sum      
def realmss(aList):
   left, mid, right = mss(aList)
   return findMax2(left,mid,right)