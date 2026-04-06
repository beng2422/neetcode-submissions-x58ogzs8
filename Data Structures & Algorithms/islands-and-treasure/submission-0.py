class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        lenx = len(grid)
        leny = len(grid[0])
        vals = [100000 for _ in range(len(grid[0]))]
        nearestDist = [vals for _ in range(len(grid))]

        def bfs(x, y):
            queue = [(x, y, 0)]


            dist = 0
            seen = []
            while queue:
                
                x,y, dist = queue[0]
                if  grid[x][y]>dist:
                    grid[x][y] = dist
                    
                queue = queue[1:]
                neighbors = []
                if x+1<lenx and (x+1,y) and grid[x+1][y] != -1 and grid[x+1][y] > dist+1:
                    seen.append((x+1,y))
                    queue.append((x+1, y, dist+1))
                if y+1<leny and (x, y+1)  and grid[x][y+1] != -1 and grid[x][y+1] > dist+1:
                    seen.append((x,y+1))
                    queue.append((x, y+1, dist+1))
                if x>0 and (x-1, y)  and grid[x-1][y] != -1 and grid[x-1][y] > dist+1:
                    seen.append((x-1,y))
                    queue.append((x-1, y, dist+1))
                if y>0 and (x, y-1)  and grid[x][y-1] != -1 and grid[x][y-1] > dist+1:
                    seen.append((x,y-1))
                    queue.append((x, y-1, dist+1))
 

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 0:
                    bfs(x, y)

        # for x in range(len(grid)):
        #     for y in range(len(grid)):
        #         if grid[x][y] == -1:
        #             grid[x][y] = -1
                # if grid[x][y] == 0:
                #     nearestDist[x][y] = -1
        print(grid)







