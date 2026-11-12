class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowerCase = s.lower()

        cleanedList = "".join(char for char in lowerCase if char.isalnum())

        #now that we have a cleaned list, then we can simply use two pointers starting
        #left and right

        left = 0
        right = len(cleanedList) - 1

        while left <= right:
            if cleanedList[left] == cleanedList[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
