class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #starting from each treasure chest we run bfs and update each value if its less

        def bfs(start):
            x, y = start
            queue = [start]
            
            visited = set()
            dist = {}
            curr_dist = 0
            
            while queue:
               

                # x, y = queue[0]
                # queue = queue[1:]
                newq = queue
                queue = []
                for x, y in newq:
                    neighbs = []
                    if dist.get((x,y), float('inf'))>curr_dist :
                        dist[(x,y)] = curr_dist
                    visited.add((x,y))
                    if x+1<len(grid) and grid[x+1][y]!=-1:
                        neighbs.append((x+1, y))
                    if x-1>=0 and grid[x-1][y]!=-1:
                        neighbs.append((x-1, y))
                    if y+1<len(grid[0]) and grid[x][y+1]!=-1:
                        neighbs.append((x, y+1))
                    if y-1>=0 and grid[x][y-1]!=-1:
                        neighbs.append((x, y-1))
                    for i in neighbs:
                        if i not in visited:
                            queue.append(i)
                curr_dist+=1
            return dist

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    dist = bfs((i,j))
                    print(dist)
                    for (i,j), val in dist.items():
                        if grid[i][j] >val:
                            grid[i][j] = val
      #  return grid











