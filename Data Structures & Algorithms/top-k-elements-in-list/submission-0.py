class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #We can keep a hashmap for each number and associate each key(num) with frequency (val)
        countMap = defaultdict(int)
        maxHeap = []
        ans = []
        for num in nums:
            countMap[num] += 1
        
        #then we can throw these into a heap and pop k times

        for key, value in countMap.items():
            #If we want to make a maxHeap, we have to order by 
            # (Frequency, number)
            maxHeap.append((-value, key)) #inverse frequency to make it a max heap
        
        heapq.heapify(maxHeap)
        for i in range(k):
            frequentElementTuple = heapq.heappop(maxHeap)
            frequentElement = frequentElementTuple[1] #value is 2nd element in tuple, freq is first
            ans.append(frequentElement)
        return ans

        

