class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        #the square number must be between 1 and num

        l = 1
        r = num

        while l <= r:
            middle = (l + r) // 2
            middleSquared = middle * middle
            if middleSquared == num:
                return True
            if middleSquared < num:
                #if less than, then we need to go higher up on our scale/spectrum of options
                l = middle + 1
            if middleSquared > num:
                #if greater than, we are too high and need to searech lower
                r = middle - 1
        return False