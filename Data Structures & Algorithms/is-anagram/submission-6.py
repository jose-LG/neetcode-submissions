class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ##we can sort is one, if they equal, then they aren't

        #basically a sorting question

        #first let's solev usinbg a hashmap

        #can also solve using sorting, maybe a heap?
        if len(s) != len(t):
            return False

        s_list = list(s)
        t_list = list(t)
        heapq.heapify(s_list)
        heapq.heapify(t_list)
        #O(n) time
        sortedS = []
        sortedT = []
        for i, charS in enumerate(s):
            minS = heapq.heappop(s_list) #should pop lexigraphically in ascending order, abcde, etc
            minT = heapq.heappop(t_list)
            sortedS.append(minS)
            sortedT.append(minT)
        return sortedS == sortedT