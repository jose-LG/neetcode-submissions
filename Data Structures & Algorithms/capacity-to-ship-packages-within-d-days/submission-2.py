class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #Max is days: int

        #Weights is not necissarily in order

        #We cannot load weight more than the maximum weight capacity of the ship

        #Return least weight capacity that allows all packages on the conveyor belt to be shipped within x days

        #We can ship as many as we want at one time, first lets think of the brute force solution and code it up

        #Suppose we had one day, then we know that the minimum capacity would have to be sum(weights)
        #If we had unlimited days, we can do very little weight capacity

        #We cannot carry 1 if capacity is zero, so lower bound on capacity is max(weights)

        #Our returned value must be maxValOf(weights) <= x <= sum(allWeights)
        #We are searching for the value closest to the left

        lowerBoundCapacity = max(weights)
        upperBoundCapacity = sum(weights)
        ans = upperBoundCapacity

        while lowerBoundCapacity <= upperBoundCapacity:
            midCapacity = (lowerBoundCapacity + upperBoundCapacity) // 2
            currDaysTest = 1

            currRunningCapacity = 0
            possible = True
            for currWeight in weights:
                if currRunningCapacity + currWeight > midCapacity:
                    currDaysTest += 1
                    currRunningCapacity = currWeight
                else:
                    currRunningCapacity += currWeight
            
            if currDaysTest <= days:
                ans = midCapacity
                upperBoundCapacity = midCapacity - 1
            else:
                lowerBoundCapacity = midCapacity + 1

        return ans