class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        #we know num is a perfect square if x * x = y
        if num == 0:
            return False
        #i.e. if there is a number for y where x * x = y
        for i in range(num + 1):
            if i * i == num:
                return True
            if i * i > num:
                break
        return False 