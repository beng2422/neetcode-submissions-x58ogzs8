class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #just run binary search twice
        def runRegularBST(currRow):
            l, r = 0, len(matrix[0]) - 1
            print('herer', currRow)
            while l <= r:
                mid = (l+r) // 2
                if matrix[currRow][mid] == target:
                    return True
                elif target > matrix[currRow][mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            return False

        l, r = 0, len(matrix) - 1
        while l <= r:
            mid = (l+r) // 2
            print(mid)
            if matrix[mid][0] <= target <= matrix[mid][len(matrix[0]) - 1]:
                return runRegularBST(mid)
            elif target > matrix[mid][len(matrix[0]) - 1]:
                l = mid + 1
            else:
                r = mid - 1
            print('newlr', l, r)
        
        return False