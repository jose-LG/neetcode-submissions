class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        #create array ans
        #append one array to another

        #brute force, we could append one element at a time in a for loop after
        #initiating 

        # 5, big O(n) time
        #linear time possible?

        concatNums = [0] * (len(nums) * 2) #we have an array of size two
        concatNums[:len(nums)] = nums #initialize the first half of the array
        concatNums[len(nums):] = nums
        return concatNums