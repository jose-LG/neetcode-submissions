class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #Fast and slow pointer approach
        if len(nums) <= 1:
            return
        
        l = 0
        r = 1

        while l < r and r < len(nums):
            #meat and potatoes, swap when l == 0 and r != 0
            if nums[l] == 0 and nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                r += 1
                l += 1
                continue
            if nums[l] != 0:
                l += 1
                #keep r in bounds
                r = max(r, l + 1)
                continue
                #this basically acts as a while loop until we encounter a swappable position
            if nums[r] == 0:
                r += 1
                continue
                

        