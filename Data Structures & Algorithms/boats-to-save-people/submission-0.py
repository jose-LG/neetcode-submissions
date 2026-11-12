class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        #So I think I actually need to sort before using two pointers for max efficiency

        people.sort() #nlogn

        left = 0
        right = len(people) - 1
        ans = 0

        while left <= right:
            if people[right] == limit:#then we can be saved rnrn
                ans += 1
                right -= 1
            else:
                #then we can search for a companion
                if people[right] + people[left] <= limit:
                    #then there is space in this setup... 
                        #Lowk we dont need to mark since we'll bump l++ and r--

                    ans += 1
                    right -= 1
                    left += 1
                else: #the lowest number is still not small enough, we need to save as an individual
                    ans += 1
                    right -= 1
        return ans