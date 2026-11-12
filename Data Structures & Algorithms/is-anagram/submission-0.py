class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #we should put each i item into a hashmap and then compare both hashmap values against eachother
        # requires one for loop and breaks as soon as there is there is not a match
        tHash = {}
        sHash = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            tHash[t[i]] = tHash.get(t[i], 0) + 1
            sHash[s[i]] = sHash.get(s[i], 0) + 1

        if tHash != sHash:
            return False

        return True
