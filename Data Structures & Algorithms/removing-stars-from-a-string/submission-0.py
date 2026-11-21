class Solution:
    def removeStars(self, s: str) -> str:
        sList = list(s) #need to subscript each
        stack = []

        for i, char in enumerate(sList):
            #if we can add to the stack (if currChar is not a star)
            if char != '*':
                stack.append(char)
            else: #then we know that char == star
                stack.pop() #and do not the current star
        return "".join(stack)