class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #start at the end, initialize the right pointer and left at end
        #push both while char == space
        #once char != space, begin coutning using the left pointer
        encounteredChar = False
        wordCount = 0

        for i in range(len(s) - 1, -1, -1):
            if encounteredChar == False and s[i] != ' ':
                #then we can know we encountered our first word
                encounteredChar = True
                wordCount += 1
                continue
            if encounteredChar == True and s[i] == ' ':
                #we just encountered the end
                return wordCount
            if encounteredChar == True and s[i] != ' ':
                wordCount += 1
        return wordCount

