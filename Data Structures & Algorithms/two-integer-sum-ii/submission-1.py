class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1 #to stay in bounds

        while l < r:
            currentSum = numbers[l] + numbers[r]
            if currentSum > target: #our solution is too large, we need to decrement to the left, toward lesser numbers!
                r -= 1
            if currentSum < target:
                l += 1
            if currentSum == target: #wohoo, solution is found
                return [l + 1, r + 1] #+1 for 1 indexed array
                #do not need another return since always one valid soltion