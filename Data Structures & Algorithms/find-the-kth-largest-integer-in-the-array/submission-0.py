import heapq
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        for i, num in enumerate(nums):
            nums[i] = -int(num)

        #casted all to an int
        heapq.heapify(nums)
        i = k - 1
        while i > 0:
            heapq.heappop(nums)
            i-= 1
        finalAns = -heapq.heappop(nums)
        return str(finalAns)
