class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left = 0
        right = len(matrix[0])-1
        top = len(matrix)-1
        bottom = 0
        res = []
        while left<= right and bottom<=top:
            
            for i in range(left, right+1):
                
                res.append(matrix[bottom][i])
            bottom += 1
            for i in range(bottom, top+1):
                res.append(matrix[i][right])
            right-=1
            if bottom<=top:
                for i in range(right, left-1, -1):
                    res.append(matrix[top][i])
            top-=1
            if left<=right:
                for i in range(top, bottom-1, -1):
                    res.append(matrix[i][left])
            left+=1

        return res
            # 2 -> 4
            # 3-> 5
            # 4-> 7
            # 5->9




            # 1 2 3 4 5
            # 5 6 7 8 6 
            # 9 8 7 6 7
            # 6 5 4 3 8 
            # 9 8 7 6 5