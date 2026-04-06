class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(node):
            visited = set()
            queue = [node]
            while queue:
                x,y = queue.pop(0)
                visited.add((x,y))
                neighbs = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
                for i, j in neighbs:
                    if 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j] == 1 and (i,j) not in visited:
                        queue.append((i,j))

            

            return visited
        ret = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    visited = dfs((i,j))
                    if len(visited)>ret:
                        ret = len(visited)
                    for (i,j) in visited:
                        grid[i][j]=0
        return ret



