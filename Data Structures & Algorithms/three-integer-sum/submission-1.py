class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #
        ans = []
        nums.sort()

        #sorting takes nlogn time

        #If we call binary search n times, that means we are running still nlogn. 2nlogn = nlogn
        
        
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]: #So we don't throw in duplicates into the ans
                continue
            #As we iterate through the array i, we can find pairs with l = i + 1
            l = i + 1
            r = len(nums) - 1

            while l < r:
                numsL = nums[l]
                numsR = nums[r]
                total = num + numsL + numsR
                if total == 0:
                    ans.append([num, numsL, numsR])
                    while l < r and nums[l] == numsL:
                        l += 1
                    while l < r and nums[r] == numsR:
                        r -= 1
                elif total > 0:
                    r -= 1
                else:
                    l += 1
        return ans