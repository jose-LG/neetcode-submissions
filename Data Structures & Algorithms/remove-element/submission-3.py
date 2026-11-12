class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        indexTracker = []
        #O(n) time
        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[left] == val:
                nums[left] = nums[right]  # overwrite bad value with rightmost
                right -= 1                # shrink window, don't move left yet
            else:
                left += 1                 # this element is fine, move on
        return left