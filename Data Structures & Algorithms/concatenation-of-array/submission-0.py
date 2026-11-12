class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans= nums
        for i in range(len(nums)):
            if i == len(nums) - 1:
                i = 0
            ans.append(nums[i])
        return ans
