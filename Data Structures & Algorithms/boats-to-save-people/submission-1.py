class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort() #nlogn time
        l = 0
        r = len(people) - 1
        numBoats = 0

        #inequality should be strict, as to avoid counting one person as two individuals
        while l <= r: #pointers
            #now we want to greedily pair the heaviest with the lightest, best case is that we pair two together and move forward with the rest
            if (people[l] + people[r]) <= limit: #then we can pair these two into a boat
                l += 1
                r -= 1
                numBoats += 1
            #if we cannot pair two, we should put the heaviest person alone on a boat and save the min values on the left
            else: # we dont even need the ineqwualityt because each persons weight is less than the limit
                #put this person on a boat and send them off
                r -= 1
                numBoats += 1
        return numBoats