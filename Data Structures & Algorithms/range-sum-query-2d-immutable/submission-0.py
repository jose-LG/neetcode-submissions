class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        #0,0 is top left, lens are at bottom right (so like normal 2d matrix)
        #Brute force approach for calcuating a single region, run a for loop in the 2d matrix
        ans = 0
        for i in range(col1, col2 + 1): #We dont want to actually go the entire column
            for j in range(row1, row2 + 1):
                ans += self.matrix[j][i]
        return ans



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)