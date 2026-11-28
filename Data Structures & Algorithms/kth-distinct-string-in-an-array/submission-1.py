class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = Counter(arr)
        distinct = set()
        for key, value in count.items():
            if value == 1: #distinct element
                distinct.add(key)
        if len(distinct) < k:
            return ""
        
        for char in arr:
            if char in distinct:
                k -= 1
            if k == 0:
                return char