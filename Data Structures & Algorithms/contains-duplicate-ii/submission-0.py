class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Ensure window doesn't exceed array bounds
        window_size = min(k + 1, len(nums))
        window = nums[:window_size]

        i = 0

        while True: # Changed condition to handle the loop logic internally
            #Now we should do all our checks and iterate at the end

            uniqueVals = set(window)

            if len(uniqueVals) < len(window): #if not all vals are unique
                return True

            if i + window_size >= len(nums):
                break

            i+=1
            # Sliding window: remove first element and append next
            window = nums[i : i + window_size]


        return False