class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = 0
        stackOfScore = []
        #Let's pop and then decide what to do next after seeing the rule

        for i, operation in enumerate(operations):
            length = len(stackOfScore)
            if operation == '+':
                #Then we want to combine the last two scores and add the result into the stack of scores
                newScore = stackOfScore[length - 1] + stackOfScore[length-2]
                stackOfScore.append(newScore)
            elif operation == 'C':
                stackOfScore.pop()
            elif operation == 'D':
                newScore = stackOfScore[-1] * 2
                stackOfScore.append(newScore)
            else:
                stackOfScore.append(int(operation))
        return sum(stackOfScore)

        