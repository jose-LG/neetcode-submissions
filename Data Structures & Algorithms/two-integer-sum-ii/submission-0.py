class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #We can take advantage of fast lookup for a set

        left = 0
        right = len(numbers) - 1

        while left < right:
            currSum = numbers[left] + numbers[right]

            if currSum == target:
                return [left + 1, right + 1]

            elif currSum > target:
                #Then we know the current sum to be too big, tone down bigness
                right -= 1
            elif currSum < target:
                left += 1
