class Solution:
    def findMin(self, nums: List[int]) -> int:
        #Lets find the trivial solution
        #What happens when we find the first number out of place?
            #I.e where nums[i + 1] < nums[i]
            #Then we know how the array has been rotated
            #The array has been rotated i times

        ans = 10000000
        for num in nums:
            ans = min(ans, num)
        return ans