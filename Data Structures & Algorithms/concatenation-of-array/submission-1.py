class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [] * len(nums) * 2
        ans.extend(nums)
        ans.extend(nums)
        return ans