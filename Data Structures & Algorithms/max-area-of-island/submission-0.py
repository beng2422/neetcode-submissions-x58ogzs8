class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        add = 0
        def dfs(node):
            x, y = node
     
            seen.append(node)

            
            neighbors = []
            if x+1<len(grid):
                neighbors.append((x+1, y))
                
            if x-1>=0:
                neighbors.append((x-1, y))

            if y+1<len(grid[0]):
                neighbors.append((x, y+1))


                
            if y-1>=0:
                neighbors.append((x, y-1))

                
            
         #   [(x+1, y) if x+1<len(grid), (x-1, y) if x-1>=0, (x, y+1) if y+1<len(grid[0]), (x, y-1) if y-1>=0]
            sumN = 1
            for neighbor in neighbors:
                newx, newy = neighbor
                if neighbor not in seen and  grid[newx][newy]==1:
                    seen.append(neighbor)
                    grid[newx][newy] = 0
                    sumN+=dfs(neighbor)
            return sumN





        seen = []
        maxV = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in seen:
                    val = dfs((i, j))
                    if val > maxV:
                        maxV = val


        return maxV





