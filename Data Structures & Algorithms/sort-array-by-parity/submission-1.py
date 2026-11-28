class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        #Brute force would be to compare each element against each other element in the input. For every element, we can see if there is a better placeement, else keep the same placement. O(n^2) lookups
        #With two poointer approach, we can simultaneously compare elements while the left pointer does not meet the right pointer
        #For eiuther side, we increment and decremenet the left and right pointers respectivelty while positions are valid
        #if a position is not valid (as in parity is out of order), then we must make a switch

       
        l = 0
        r = len(nums) - 1
        while l <= r:
            if nums[l] % 2 == 1 and nums[r] % 2 == 0 : #if left num is odd and right num is even, make a switch mf
                nums[l], nums[r] = nums[r], nums[l] #in python we can make quick swaps in one line
                l += 1
                r -= 1
            if nums[r] % 2 == 1: #right is odd
                r -= 1
            if nums[l] % 2 == 0: #left is even
                l += 1
        return nums