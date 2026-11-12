class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #Now we are on heaps

        #Two heaviest stones means we need a max heap
        maxHeap = []
        for stone in stones:
            maxHeap.append(-stone) #heaps are min by default so min heap with reverted vals in max heap

        heapq.heapify(maxHeap)
        while len(maxHeap):
            if len(maxHeap) < 2:
                #means we may only have 1 or 0 elements left
                if len(maxHeap) == 1:
                    return heapq.heappop(maxHeap) * -1
                else:
                    return 0

            heaviestStone = heapq.heappop(maxHeap) * -1 #must invert to the normal number to do the comparison
            smallerStone = heapq.heappop(maxHeap) * -1

            if heaviestStone == smallerStone:
                continue
            elif smallerStone < heaviestStone:
                heapq.heappush(maxHeap, abs(heaviestStone - smallerStone) * -1) #we have to retain the negative value to persist a maxHeap
        return 0