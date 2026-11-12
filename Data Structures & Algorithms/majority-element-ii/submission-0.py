class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        #find all nums that appear more than n/3 times

        #if we use a hashmap and do a single pass, then we can run through the the hashmap
        #Elements for an O(n) time solution, but space is > O(1).

        #To do in O(1) space, we have to calculate this in place

        #Lets still do the hashmap solution as warmup

        hashmap = defaultdict(int)
        threshold = len(nums) // 3
        ans = []
        for num in nums:
            hashmap[num] += 1 #now we have the count of all values
        for key, value in hashmap.items():
            if value > threshold:
                ans.append(key)
        return ans