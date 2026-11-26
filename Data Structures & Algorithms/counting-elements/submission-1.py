class Solution:
    def countElements(self, arr: List[int]) -> int:
        counter = 0
        arrSet = set(arr) #O(1)lookip

        for i, num in enumerate(arr):
            currValue = arr[i]
            if currValue + 1 in arrSet:
                counter += 1
        

        return counter