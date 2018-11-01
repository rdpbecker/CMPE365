def setUnion(vertices,new):
    flag = 1
    newSet = []
    for vertex in vertices:
        if vertex == new:
            flag = 0
        newSet.append(vertex)
    if flag:
        newSet.append(new)
    return newSet

def setIntersect(set1,set2):
    inBoth = {}
    newSet = []
    for thing in set1:
        inBoth[thing] = 1
    for thing in set2:
        if thing in inBoth.keys():
            newSet.append(thing)
    return newSet

def numToBinary(n,length):
    aList = []
    for i in range(length-1,-1,-1):
        k = n/(2**i)
        aList.append(k)
        n = n - k*(2**i)
    return aList

def binaryToList(aList,binList,length):
    endList = []
    for i in range(length):
        if binList[i]:
            endList.append(aList[i])
    return endList

def listToNum(aList,maxVal):
    num = 0
    for n in aList:
        num = num + 2**(maxVal-n)
    return num

def numToSet(num,maxVal):
    aSet = []
    for i in range(1,maxVal+1):
        k = num/(2**(maxVal-i))
        if k:
            aSet.append(i)
        num = num - k*(2**(maxVal-i))
    return aSet

def subsetsByIndex(aList,maxVal):
    length = len(aList)
    subsetList = []
    for i in range(2**length-1,-1,-1):
        subsetList.append(listToNum(binaryToList(aList,numToBinary(i,length),length),maxVal))
    return subsetList

if __name__ == "__main__":
    import sys
    length = len(sys.argv)-1
    maxVal = int(sys.argv[-1])
    aList = []
    for i in range(1,length):
        aList.append(int(sys.argv[i]))
    print numToSet(listToNum(aList,maxVal),maxVal)
