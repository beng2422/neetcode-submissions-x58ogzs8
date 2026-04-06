class Solution:
    def solve(self, board: List[List[str]]) -> None:
        lenx = len(board)
        leny = len(board[0])

        def bfs(x, y):
            queue = [(x, y)]
            values = []
            seen = []
            surround = [(x+1, y+1), (x-1, y+1), (x+1, y-1), (x-1, y-1)]

            while queue:
                x, y = queue[0]
                queue = queue[1:]
                values.append((x,y))
                 
            
                if y+1<leny and board[x][y+1] == 'O' and (x, y+1) not in seen:
                    queue.append((x, y+1))
                    seen.append((x, y+1))
                    surround[0] = (x+1, y+2)
                    surround[1] = (x-1, y+2)
                if x+1<lenx and board[x+1][y] == 'O' and (x+1, y) not in seen:
                    queue.append((x+1, y))
                    seen.append((x+1, y))
                    surround[0] = (x+2, y+1)
                    surround[2] = (x+2, y-1)
                if x-1>0 and board[x-1][y] == 'O' and (x-1, y) not in seen:
                    queue.append((x-1, y))
                    seen.append((x-1, y))
                    surround[1] = (x-2, y+1)
                    surround[3] = (x-2, y-1)
                if y-1>0 and board[x][y-1] == 'O' and (x, y-1) not in seen:
                    queue.append((x, y-1))
                    seen.append((x, y-1))
                    surround[2] = (x+1, y-2)
                    surround[3] = (x-1, y-2)
            return values, surround
        for x in range(lenx):
            for y in range(leny):
                if board[x][y] == 'O' :
                    values, surround = bfs(x, y)
                    print(values)
                    truehere = False
                    for x, y in surround:
                        if 0<=x and x< lenx and 0<=y and y<leny:
                            truehere = True
                        else:
                            truehere = False
                            break
                    if truehere: 
                        for x, y in values:
                            board[x][y] = 'X'

        print(board)








        