class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        vals = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    vals.append((i, j))

        for (i,j) in vals:
            for k in range(len(matrix)):
                matrix[i][k] = 0
                matrix[k][i] = 0