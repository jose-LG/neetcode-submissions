class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        word1Concatenated = "".join(word1)
        word2Concatenated = "".join(word2)
        if word1Concatenated == word2Concatenated:
            return True
        else:
            return False
        
