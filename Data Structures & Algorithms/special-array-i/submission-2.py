class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        lastOdd = False

        for i, num in enumerate(nums):
            if i == 0:
                if num % 2 == 1:
                    lastOdd = True
                continue

            #[VALID] is num is odd and last num was even 
            if num % 2 == 1 and lastOdd == False:
                lastOdd = True
                continue

            #[VALID]if num is even and last num is odd
            if num % 2 == 0 and lastOdd == True:
                lastOdd = False
                continue

            #[ERROR]If num is even and last num was even
            if num % 2 == 0 and lastOdd == False:
                return False
            
            #[ERROR] if num is odd and last num was odd
            if num % 2 == 1 and lastOdd == True:
                return False
            #then we need our switch case for when we see a valid even number
        return True