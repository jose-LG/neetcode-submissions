class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1

        while left < right:
            leftVal = s[left]
            rightVal = s[right]

            s[left] = rightVal
            s[right] = leftVal
            #now they're fully switched
            left += 1
            right -= 1
        