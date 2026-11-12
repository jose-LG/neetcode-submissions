class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #How do we define the "max amount"

        #We need B x H

        #H is top 2 elements



        #By the graph, it looks like max is the top two elements 

        left = 0
        right = len(heights) - 1
        ans = 0
        while left < right:
            #calculate current area each turn

            area = min(heights[left], heights[right]) * (right - left)
            ans = max(ans, area)

            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return ans

