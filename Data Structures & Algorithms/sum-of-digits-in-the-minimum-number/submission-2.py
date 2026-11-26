class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        minNumberAsList = list(str(min(nums)))
        sumNums = 0
        for i, num in enumerate(minNumberAsList):
            sumNums += int(num)
        if sumNums % 2 == 0:
            return 1
        else:
            return 0

        
