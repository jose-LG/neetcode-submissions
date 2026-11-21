class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        l = 0
        r = len(tokens) - 1
        maxScore = 0
        currScore = 0
        tokens.sort()
        nums = tokens

        while l <= r:
            #naive condition, keep consuming left to right until power < nums[l]
            if nums[l] <= power:
                currScore += 1
                maxScore = max(currScore, maxScore)
                power -= nums[l]
                l += 1 #keep pushing toward the right
            #Now what happens if we cannot consume but we want to try to steal from the right? We can be greedy by selecting the largest token to trade for power
            elif (nums[r] + power) > nums[l] and currScore > 0: #then we are in a safe position to consume
                power += nums[r]
                currScore -= 1
                r -= 1 #cannot use that token since we have consumed it
            else:
                #we cannot consume and we cannot keep pushing toward the left, we can return maxScore
                return maxScore
        return maxScore
