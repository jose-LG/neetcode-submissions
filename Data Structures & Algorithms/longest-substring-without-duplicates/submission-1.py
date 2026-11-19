class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longestSS = 0

        if len(s) == 0:
            return 0

        currSet = set()

        for r, char in enumerate(s):
            if s[r] not in currSet:
                #we should append this number to the set and check our max length
                currSet.add(s[r])
                longestSS = max(len(currSet), longestSS)
            else: #the wanting to be appended value is in the set
                #We have to continue until the right value is not in the set, at which point we can now add the right value and continue with the algo
                while s[r] in currSet:
                    currSet.remove(s[l])
                    l += 1 #bump forward to try the next
                #Now we can safely add right value to our window
                currSet.add(s[r])
                longestSS = max(len(currSet), longestSS) #lowkey this should always be less than the max since we just rm a bunch of stuff
        return longestSS
