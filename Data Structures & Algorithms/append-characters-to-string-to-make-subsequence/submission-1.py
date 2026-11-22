class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        sPointer = 0
        tPointer = 0
        seen = []
        while sPointer < len(s) and tPointer < len(t):
            #best case is that we see both, bump both, and add to seen array
            if s[sPointer] == t[tPointer]:
                seen.append(t[tPointer])
                tPointer += 1
            
            sPointer += 1
        return abs(len("".join(seen)) - len(t))