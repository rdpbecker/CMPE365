import part1, copy

def findIndexes(aList, sublist):
    n = len(sublist)
    for index in range(len(aList)):
        if aList[index:index+n] == sublist:
            return index, index+n

def min(aList):
   min = 0
   for i in range(len(aList)):
      if aList[i] < min:
         min = aList[i]
   return min
   
def allZeroes(aList):
   for i in range(len(aList)):
      if aList[i] = 0:
         return 0
   return 1

def bothLargest(aList):
   largest = part1.realmss(copy.deepcopy(aList))
   print "The largest sum is", part1.sum(largest)
   print "The largest sublist is", largest, '\n'

   start, end = findIndexes(aList,largest)
   minVal = min(aList)
   replacement = [minVal] * len(largest)
   aList[start:end] = replacement
   if len(replacement) == len(aList) or allZeroes(aList):
      print "Largest sublist is the whole list - cannot find the second largest"
      return
   
   second = part1.realmss(copy.deepcopy(aList))
   print "The second largest sum is", part1.sum(second)
   print "The second largest sublist is", second

# Check the example given
list0 = [2,4,5,-7,3,-6,1,4]
# Check a list with a length of a power of two
list1 = [1,-3,5,7,8,1,-3,1,-7,-1,2,3,-5,4,2,6] 
# Check a list with a length not a power of two
list2 = [1,-3,5,7,1,-3,1,-7,2,3,-5,4,6] 
# Check a list whose sublist with the largest sum is the whole list
list3 = [1,2,3,4,5,6,7,8,8,7,6,5,4,3,2,1]
# Check a variation on the last one with one element excluded
list4 = [-1,2,3,4,5,6,7,8,8,7,6,5,4,3,2,1]
# Check a list whose sublist with the largest sum contains a 
# negative number
list5 = [1,3,4,-3,4,5,-8,-9,1,2,3,4,-5,6]
# And another one
list6 = [-20,2,3,4,-2,6,7,-8,-10,4,7,-13,8,-5,2,6,-8,10,-12,-2]
# Check a list with all negative values
list7 = [-2,-3,-4,-1,-17,-13,-9,-200,-34]
# Check a list whose subtree with the largest sum is repeated twice
list8 = [1,5,7,8,-12,-3,-15,1,5,7,8,-4]
# Check a list with two different sublists whose sum is the maximum
list9 = [7,6,-1,-2,-15,1,6,4,2]
# Check a list with some 0s in it
list10 = [1,-3,0,5,0,7,1,0,-3,1,-7,2,3,-5,4,6]
# Check a list whose entries are all equal and positive except a 
# block in the middle
list11 = [1,1,1,1,1,1,3,3,3,3,1,1,1,1,1]
# Check a list whose entries are all equal and negative except a 
# block in the middle
list12 = [-1,-1,-1,-1,-1,-1,3,3,3,3,-1,-1,-1,-1,-1]
# Check a list whose maximal sublist is not the whole list but which contains only 0s after replacing the maximal sublist
list13 = [0,1,2,3,4,5,6,7,7,6,5,4,3,2,1,0]

bothLargest(list13)