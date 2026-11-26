class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        #input: array of nums\
        #output: num of 1s in a row = highest sum window
        #sliding window with variable k
        maxConsecutive = float("-inf")
        counter = 0

        for i, num in enumerate(nums):
            if num == 0: #reset the counter
                counter = 0
            else:
                counter += 1
            maxConsecutive = max(counter, maxConsecutive)
        return maxConsecutive
