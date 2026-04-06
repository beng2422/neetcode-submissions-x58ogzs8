class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        #Run dfs on each value - WRONG
        #Create a new node attached to pacific and atlantic 
        #Run dfs on both sides - keep track of the paths that get you from 
        #pacific to atlantic or vice versa
        #


        row = len(heights)
        col = len(heights[0])

        def dfs(pacific):
            stack = []
            visited = set()

            if pacific:
                for i in range(col):
                    stack.append((0, i))
                    visited.add((0, i))
                for i in range(row):
                    stack.append((i, 0))
                    visited.add((i, 0))
            else:
                for i in range(col):
                    stack.append((row-1, i))
                    visited.add((row-1, i))
                for i in range(row):
                    stack.append((i, col-1))
                    visited.add((i, col-1))

            flowable = set()
            


            while stack:
                (x, y) = stack.pop()
                # if (x, y) not in seen:
                #     seen.append((x, y))
   
                for (i, j) in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                    if 0<=i and i<row and 0<=j and j<col and heights[i][j]>=heights[x][y] and (i, j) not in visited:
                        flowable.add((i, j))
                        stack.append((i, j))
                        visited.add((i,j))
            return visited

        pacific = dfs(True)
        atlantic = dfs(False)
        ret = []
        for i in pacific:
            if i in atlantic:
                ret.append(i)
        return ret







