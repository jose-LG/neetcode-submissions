class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)

        for i, num1 in enumerate(nums):
            productForNum1 = 1
            for j, num2 in enumerate(nums):
                if i != j:
                    productForNum1 *= num2
            
            ans[i] = productForNum1
        return ans