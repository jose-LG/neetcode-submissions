class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #create a hashmap
        #check against the hashmap at every check in the for loop

        newSet = set(nums)
        if len(newSet) < len(nums):
            return True
        else:
            return False
        
        