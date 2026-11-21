class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        #Insight: We know the length of the array and the highest number i can be is len(array) and lowest it can be is zero
        l = 0
        r = len(arr) - 1
        ans = -1

        while l <= r: #in this case we can be the same number since we are just checking for when arer[i] == i
            middle = (l + r) // 2
            if arr[middle] >= middle:
                if arr[middle] == middle:
                    ans = middle
                r = middle - 1
            else:
                #we are too small and we need to try toward the right
                l = middle + 1
        return ans