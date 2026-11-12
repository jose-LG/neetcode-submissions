class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #we know that it takes Big o(n) to turn a array into a set
        setNums = set(nums)
        if len(nums) != len(setNums):
            #We knoe that the array contains dupes!
            return True
        else:
            return False
        
        