class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix=[]
        sum_r=0
        row=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                sum_r+=matrix[i][j]
                row.append(sum_r)
            sum_r=0
            self.matrix.append(row)
            row=[]
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sumR=0
        for i in range(row1,row2+1):
            sub = 0 if [col1]==[0] else self.matrix[i][col1-1]
            sumR+=(self.matrix[i][col2]-sub)
        return sumR
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
