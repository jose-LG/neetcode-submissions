class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        #to avoid repeated work, we want to collect the forward running and backward running sums only once
        prefixSum = [0] * len(nums)
        suffixSum = [0] * len(nums)
        runningSum = 0
        maxSumScore = float('-inf')
        for i, num in enumerate(nums):
            runningSum += num
            prefixSum[i] = runningSum #inclusive
        
        #now we should go backward
        runningSum = 0
        for i in range(len(nums) - 1, -1, -1): #-1 is non,inclusive
            runningSum += nums[i]
            suffixSum[i] = runningSum
        #now that we have all of our prefix and suffixSum sorted, we can run through each element once
        #and compare between the suffixSum and the runningSum
        for i, num in enumerate(nums):
            maxSumScore = max(maxSumScore, max(prefixSum[i], suffixSum[i]))
        return maxSumScore