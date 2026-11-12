class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #distinct
        left = 0
        right = len(nums) - 1
        mid = 0
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        if target > nums[mid]:
            return mid + 1
        else:
            return mid
            




