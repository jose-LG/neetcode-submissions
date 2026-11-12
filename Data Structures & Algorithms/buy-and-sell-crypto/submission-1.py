class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        [10, 11, 1, 6, 1, 7]

        #Two pointers
        #When l > r, then we slide the window to l = r and r = l+1

        #When we make some time of profit, we have to record it somewhere "max(currAns, ans)"
        maxProfit = 0
        if len(prices) < 2:
            return maxProfit
        
        l = 0
        r = 1

        while r < len(prices):
            maxProfit = max(prices[r] - prices[l], maxProfit) #when no profit is made, it is handled bc of negative vals
            if prices[l] > prices[r]: #then some profit can be made here....
                l,r = r,r+1
            else:
                r += 1
        return maxProfit


