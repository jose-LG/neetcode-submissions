class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        minHeap = []
        ans = []

        for i, point in enumerate(points):
            distance = math.pow(point[0], 2) + math.pow(point[1], 2)
            minHeap.append((distance, point)) #format is (distance, [1, 1]) for example
            #this way, we can heapify with the first element, using n extra memory
        heapq.heapify(minHeap) #now a minheap by default, we can pop the first K elements using a for loop

        for i in range(k):
            closestPointDistance = heapq.heappop(minHeap) #format is (distance, pointArray)
            closestPoint = closestPointDistance[1]
            ans.append(closestPoint)
        return ans