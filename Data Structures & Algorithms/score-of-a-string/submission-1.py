class Solution:
    def scoreOfString(self, s: str) -> int:
        runningSum = 0
        for i, char in enumerate(s):
            prevOrdValue = 0
            nextOrdValue = 0
            currOrdValue = ord(char)
            #inbounds check for both less than 0 and greater than length
            if i - 1 >= 0:
                #out of bounds on left, cant check prev value
                prevOrdValue = ord(s[i - 1])
                valueToBeAdded = abs(prevOrdValue - currOrdValue)
                runningSum += valueToBeAdded
            
            #we dont add it outside the bounds check because we dont want to add add the difference between null and the leftmost andf rightmost valyes
        return runningSum
            