class Solution:
    def countElements(self, arr: List[int]) -> int:
        counter = 0

        for i, num in enumerate(arr):
            currValue = arr[i]
            if currValue + 1 in arr:
                counter += 1
        

        return counter