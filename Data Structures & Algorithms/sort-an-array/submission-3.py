class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #We can sort using binary sort
        ans = []
        heapq.heapify(nums)
        while nums:
            minVal = heapq.heappop(nums)
            ans.append(minVal)
        return ans