class Solution:
    def isValid(self, s: str) -> bool:
        #we can do this with two pointers or a stack?? But with two pointers it's kind of the same thing
        #Solve first with a stack

        openBracketsStack = []
        closedBracketsStack = []
        openBrackets = ["(", "{", "["]
        closedBrackets = [")", "}", "]"]


        for char in s:
            if char in openBrackets:
                openBracketsStack.append(char)
            elif not openBracketsStack and char in closedBrackets:
                return False
            elif openBracketsStack and self.matchesBracket(char, openBracketsStack[-1]) == False:
                return False
            else:
                openBracketsStack.pop() #we can pop because it's a valid str and doesnt need to be checked anymore
        if len(openBracketsStack) > 0:
            return False
        else:
            return True
        
    def matchesBracket(self, potentialMatch: str, openBracket: str) -> bool:
        if openBracket == "(":
            return potentialMatch == ")"
        elif openBracket == "{":
            return potentialMatch == "}"
        elif openBracket == "[":
            return potentialMatch == "]"
            
