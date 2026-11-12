class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #unsorted array, return the kth largest element (one number)
        #remember, heaps are min by default so we have to run through in at least n
        #and convert the values to maxHeap
        
        elements = []
        for num in nums:
            elements.append(-num)
        
        heapq.heapify(elements) #now we have a maxHeap

        for i in range(k - 1):
            heapq.heappop(elements)
        return -heapq.heappop(elements) #have to return negative because it's a maxHeap