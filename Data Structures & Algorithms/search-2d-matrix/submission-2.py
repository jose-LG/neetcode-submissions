class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Ascending order with duplicates
        #we can define a binary search helper that runs binary search for each entity

        # that way, we can split the inputs in half and split the input's arrays in half
        lowerArray = 0
        highArray = len(matrix) - 1

        while lowerArray <= highArray:
            middleListNum = (lowerArray + highArray) // 2 #gives how many columns are in the array // 2
            middleList = matrix[middleListNum]
            lowestValue, highestValue = middleList[0], middleList[-1]
            if lowestValue <= target <= highestValue: #We can't just return True bc the value may be absent, so we need to run the official search
                return self.binarySearch(middleList, target)
            elif target < lowestValue:
                #then we need to look more on the left side (still cold near the lowestVal, go lower)
                highArray = middleListNum - 1
            elif target > highestValue:
                lowerArray = middleListNum + 1
        return False



    
    def binarySearch(self, midList: List, target: int):
        left = 0
        right= len(midList) - 1

        while left <= right:
            midpoint = (left + right) // 2

            if midList[midpoint] == target:
                return True
            elif midList[midpoint] < target:
                left = midpoint + 1
            elif midList[midpoint] > target:
                right = midpoint - 1
        return False