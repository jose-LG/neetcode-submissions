class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #return k most frequent elements
        #Insight: we somehow want to obtain a count of each
        #If we want to check every element and be sure
        #We can iterate over the array and have a counter for each number
        #In a hashmap

        hashmap = defaultdict(int)

        for num in nums:
            hashmap[num] += 1 #now we have all
        
        #We can order a heap with maxHeap where the tuple[0] is count and tuple[1] is num
        heap = []
        ans = []
        for num, count in hashmap.items():
            heap.append((-count, num))
        heapq.heapify(heap)

        while k > 0:
            ans.append(heapq.heappop(heap)[1])
            k -= 1
        return ans


















