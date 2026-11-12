class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""

        for i in range(min(len(word1), len(word2))): #This way we will never hit an out of bounds
            ans = ans + (word1[i] + word2[i]) #add the most recent letters to the ans 
        
        if len(word1) == len(word2): #then our job here is done
            return ans
        elif len(word1) < len(word2):
            #Word 1 is longer
            ans = ans + word2[len(word1):]
            return ans
        else:
            ans = ans + word1[len(word2):]
            return ans
        return ans

