class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # ideas - turn this matrix into a graph


        #what data struct should I use? 
        #[[(x, y), (x, y)]] - this is inefficient - would have to traverse all existing ones (O(m^2n))
        #Graph using a class that initializes nodes with children
        #Could we use dfs or bfs? Yes


        seen = set()
        island_count = 0
        for x1 in range(len(grid)):
            for y1 in range(len(grid[0])):

                if grid[x1][y1] == "1" and (x1, y1) not in seen:
                    stack = [(x1, y1)]
                    seen.add((x1, y1))
                    
                    while stack:

                        x, y = stack.pop()
                        seen.add((x, y))

                        if 0<= x+1 and x+1<len(grid) and grid[x+1][y] == '1' and (x+1, y) not in seen:
                            stack.append((x+1, y))
                            seen.add((x+1, y))
                        if 0<= x-1 and x-1<len(grid) and grid[x-1][y] == '1' and (x-1, y) not in seen:
                            stack.append((x-1, y))
                            seen.add((x-1, y))
                        if 0<= y+1 and y+1<len(grid[0]) and grid[x][y+1] == '1' and (x, y+1 )not in seen:
                            stack.append((x, y+1))
                            seen.add((x,y+1))
                        if 0<= y-1 and y-1<len(grid[0]) and grid[x][y-1] == '1' and (x, y-1) not in seen:
                            stack.append((x, y-1))     
                            seen.add((x, y-1))                     

                    island_count +=1 
        return island_count


        