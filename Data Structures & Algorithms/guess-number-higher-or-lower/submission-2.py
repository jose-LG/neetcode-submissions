# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        lower = 1
        end = n

        while lower <= end:
            midNum = (end + lower) // 2

            if guess(midNum) == 0:
                return midNum
            elif guess(midNum) == -1:
                end = midNum - 1
            elif guess(midNum) == 1:
                lower = midNum + 1