class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #array nums
        #size n
        #Majority element appears more than 50% of the time
        #Always exists

        #if we through in a hashmap, we can check for the longest in 
        
        hashmap = {}
        #By the last number, we already have the hashmap filled so we can track as we go... probably haha
        highestOccurances = 0
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
            highestOccurances = max(highestOccurances, hashmap.get(num))
        
        for key, val in hashmap.items():
            if highestOccurances == val:
                return key


