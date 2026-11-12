class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowerCase = s.lower()

        cleanedList = "".join(char for char in lowerCase if char.isalnum())

        #now that we have a cleaned list, think about symmetricalness now

        left = 0
        right = len(cleanedList) - 1

        while left <= right:
            if cleanedList[left] != cleanedList[right]:
                return False
            left +=1
            right -=1
        
        return True
            
