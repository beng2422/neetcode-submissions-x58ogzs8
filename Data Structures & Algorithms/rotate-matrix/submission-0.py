class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        res = []
        matrix2=matrix.copy()
        
        for i in range(len(matrix2)):
            val = []
            for j in range(len(matrix2)):
                val.append(matrix2[j][i])
            
            matrix[i] = val
        
        for i in range(len(matrix2)):
            val = []
            for j in range(len(matrix2)-1, -1, -1):
                val.append(matrix[i][j])
            
            matrix[i] = val


