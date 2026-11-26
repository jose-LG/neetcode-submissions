class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        numsCountMap = defaultdict(int)
        maxInt = -1

        for i, num in enumerate(nums):
            numsCountMap[num] += 1
        #Now we have the count of all
        for key, value in numsCountMap.items():
            if key > maxInt and value == 1: #occurs only once and a newMaxInt
                maxInt = key #in this case, key is always greater and
        return maxInt
