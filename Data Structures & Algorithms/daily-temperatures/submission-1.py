class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] #(Te4mp, index format)
        ans = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and temp> stack[-1][0]:
                stackTemp, stackInd = stack.pop()
                ans[stackInd] = (i - stackInd)
            stack.append([temp, i])
        return ans