class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ctr=0
        for i,j in enumerate(matrix):
            k=ctr
            while  k<len(j):
                if k!=i:
                    matrix[i][k],matrix[k][i]=matrix[k][i],matrix[i][k]
                k+=1
            ctr+=1
        n=len(matrix[0])
        half=n//2
        for j,i in enumerate(matrix):
            ctr=0
            while ctr<half:
                matrix[j][ctr],matrix[j][n-1-ctr]=matrix[j][n-1-ctr],matrix[j][ctr]
                ctr+=1        
