class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ##we can sort is one, if they equal, then they aren't

        #basically a sorting question

        #first let's solev usinbg a hashmap

        if len(s) != len(t):
            return False

        hashmapS = defaultdict(int)
        hashmapT = defaultdict(int)


        for charS, charT in zip(s, t):
            hashmapS[tuple(charS)] = hashmapS.get(tuple(charS), 0) + 1 
            hashmapT[tuple(charT)] = hashmapT.get(tuple(charT), 0) + 1 

        return hashmapS == hashmapT