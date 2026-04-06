class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        lenx = len(grid)
        leny = len(grid[0])
        queue = []
        time = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 2:
                    queue.append((x, y, 0))
        while queue:
            x, y, time = queue[0]
            queue = queue[1:]


            if x+1<lenx and grid[x+1][y] == 1:
                grid[x+1][y] = 2
                queue.append((x+1, y, time+1))
            if y+1<leny and grid[x][y+1] == 1:
                grid[x][y+1] = 2
                queue.append((x, y+1, time+1))
            if x>0 and grid[x-1][y] == 1:
                grid[x-1][y] = 2
                queue.append((x-1, y, time+1))
            if y>0 and grid[x][y-1] == 1:
                grid[x][y-1] = 2
                queue.append((x, y-1, time+1))

        print(grid)
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] ==1:
                    return -1
        return time



