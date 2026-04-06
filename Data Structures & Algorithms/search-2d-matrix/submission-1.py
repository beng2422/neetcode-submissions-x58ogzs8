class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #first do a binary search through the leftmost column to see if its less than or equal to
        #then do a binary search through the row
        correctRow = 0
        b = 0
        t = len(matrix)-1
        leftMost = len(matrix[0])-1
        while b<=t:
            mid = (t+b)//2
            #case when its in that row
            print('val', matrix[mid][leftMost])
            print('val2', matrix[mid-1][leftMost])
            if (mid>0 and matrix[mid-1][leftMost] < target < matrix[mid][leftMost]) or (mid==0 and target < matrix[mid][leftMost]):

                correctRow = mid
                print('mid here', mid)
                break
            elif (matrix[mid][leftMost]>target):
                b = mid+1
            else:
                t=mid-1
            print('t', t, 'b', b, 'mid', mid)
        l, r = 0, len(matrix[0])-1
        while l<=r:
            mid = (l+r)//2
            if matrix[correctRow][mid]==target:
                return True
            elif matrix[correctRow][mid]<target:
                l=mid+1
            else:
                r = mid-1

        print('row', correctRow)
        return False













