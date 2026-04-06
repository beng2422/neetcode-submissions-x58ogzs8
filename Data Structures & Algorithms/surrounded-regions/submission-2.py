class Solution:
    def solve(self, board: List[List[str]]) -> None:
        lenx = len(board)
        leny = len(board[0])

        def bfs(x, y):
            queue = [(x, y)]
            values = []
            seen = []
            surround = [(x+1, y+1), (x-1, y+1), (x+1, y-1), (x-1, y-1)]
            border_touch = (x == 0 or x == lenx-1 or y == 0 or y == leny-1)  # <---

            while queue:
                x, y = queue[0]
                queue = queue[1:]
                values.append((x,y))
                 
                if x == 0 or x == lenx-1 or y == 0 or y == leny-1:          # <---
                    border_touch = True
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
            return values, surround, border_touch
        for x in range(lenx):
            for y in range(leny):
                if board[x][y] == 'O' :
                    values, surround, border_touch = bfs(x, y)
                    print(values)
                    truehere = False
                    for xin, yin in surround:
                        if 0<=xin and xin< lenx and 0<=yin and yin<leny:
                            truehere = True
                        else:
                            truehere = False
                            break
                    if truehere: 
                        for xh, yh in values:
                            board[xh][yh] = 'X'
                    if (not border_touch) and truehere:                           # <---
                        for xh, yh in values:
                            board[xh][yh] = 'X'
        print(board)








        