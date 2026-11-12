class Solution:
    def mySqrt(self, x: int) -> int:
        #Key Inutiion of a square root:
        lower = 0 #include zero for when x = 0
        higher = x #just to make it easy on ourselves now


        while lower <= higher:
            currTest = (higher+ lower) // 2
            currTestSquared = currTest * currTest

            if currTestSquared == x:
                return currTest
            elif currTestSquared < x:
                lower = currTest + 1
            elif currTestSquared > x:
                higher = currTest - 1
        #Since while loop runs until lower and higher are equal, we can return.... when they are equal, so either
        #Takes nlogn time
        return higher