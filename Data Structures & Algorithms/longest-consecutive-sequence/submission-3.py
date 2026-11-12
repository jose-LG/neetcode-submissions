class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #for num in nums
        #Each time we pass through, we add to hashmap if not already
        #Then for each num, we check if there is a key with the num
        if not nums:
            return 0

        numsSet = set(nums)
        ans = 1
        for num in nums:
            if num - 1 not in numsSet: #then we know it is the beginning of the sequence
                currLongest = 1
                sequenceStart = num
                while sequenceStart + 1 in numsSet:
                    sequenceStart += 1
                    currLongest += 1
                #now that we've found all of the currentLongest
                ans = max(ans, currLongest)
        return ans

