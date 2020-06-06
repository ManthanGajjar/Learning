import math

class BinarySearch():
    def performSearchOpration(self, arrayOfList, target):
        newMidIndex = int(math.floor(len(arrayOfList) / 2 ))
        return BinarySearch.recursiveMethod(self, arrayOfList, target, 0, len(arrayOfList), newMidIndex)
    
    def recursiveMethod(self, arrayOfList, target, startIndex, endIndex, midIndex):
        if(midIndex >= endIndex):
            return -1

        if(arrayOfList[midIndex] == target):
            return midIndex
        
        if(arrayOfList[midIndex] > target ):
            newMidIndex = int(math.floor((midIndex) / 2 ))
            return BinarySearch.recursiveMethod(self, arrayOfList, target, 0,midIndex, newMidIndex )
        else:
            newMidIndex = int(math.floor((midIndex + endIndex) / 2 ))
            return BinarySearch.recursiveMethod(self, arrayOfList, target, midIndex, endIndex, newMidIndex)
    


listOfValue = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18, 19, 20]
target = 30
classInstance = BinarySearch()
result = classInstance.performSearchOpration(listOfValue, target)

print("Can't find the element in search result... " if result == -1 else f"element found at POS {result}")
