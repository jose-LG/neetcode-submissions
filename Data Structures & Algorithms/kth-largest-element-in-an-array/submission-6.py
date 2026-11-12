class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #unsorted array, return the kth largest element (one number)
        #remember, heaps are min by default so we have to run through in at least n
        #and convert the values to maxHeap

        heapq.heapify(nums)

        #we can save memory by returning len - kth element

        for i in range(len(nums) - k):
            heapq.heappop(nums)

        return heapq.heappop(nums)