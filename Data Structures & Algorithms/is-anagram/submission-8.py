class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #we want to understand how many occurences there are of each letter
        #in each word

        #We could make a hashmap, that would require us to iterare through each string and iterate the counts. We could have different maps for each word and at the end, we can compare each key, and then compare the counts for each key in each map

        #Now this would take a lot of space
        #Insight: there are 26 letters in the alphabet, so we know that the choices of letters are very limited

        #We can create an "alpha" array for each string of length 26, where each index represents the count for that letter in the alphabet. 
        #Base case, when lengths do not match

        if len(s) != len(t):
            return False
        
    

        sAlphabet = [0] * 26 #letters in the alpha 
        tAlphabet = [0] * 26

        #Normalize ascii values to match a = 0, b = 1, c = 2, etc
        s.lower()
        t.lower()
        #same length
        for i in range(len(s)):
            #we want the ascii value of how many spaces away from "a" is this?
            sAsciiVal = abs(ord(s[i]) - ord("a")) #always nonnegative
            tAsciiVal = abs(ord(t[i]) - ord("a")) #always nonnegative
            sAlphabet[sAsciiVal] += 1
            tAlphabet[tAsciiVal] += 1
        return tAlphabet == sAlphabet













