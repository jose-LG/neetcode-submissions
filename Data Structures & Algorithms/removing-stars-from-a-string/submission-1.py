class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for i, char in enumerate(s):
            #if we can add to the stack (if currChar is not a star)
            if char != '*':
                stack.append(char)
            else: #then we know that char == star
                stack.pop() #and do not the current star
        return "".join(stack)