class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #4 recursions - left, right, down, up
        #curr = [(), ()] - tuple x, y corresponding to places its already been
        max_x = len(board[0])
        max_y = len(board)
        def dfs(curr, val, curr_tuple):
            if '' == val:
                return True
            x, y = curr_tuple
            if (x+1, y) not in curr and max_x>x+1 and board[y][x+1] == val[0]:
                curr.append((x+1, y))
                if  dfs(curr, val[1:], (x+1, y)):
                    return True
            if (x-1, y) not in curr and 0<x-1 and board[y][x-1] == val[0]:
                curr.append((x-1, y))
                if dfs(curr, val[1:], (x-1, y)):
                    return True

            if (x, y+1) not in curr and max_y>y+1 and board[y+1][x] == val[0]:
                curr.append((x, y+1))
                if  dfs(curr, val[1:], (x, y+1)):
                    return True
            if (x, y-1) not in curr and 0<y-1 and board[y-1][x] == val[0]:
                curr.append((x, y-1))
                if dfs(curr, val[1:], (x, y-1)):
                    return True

            return False
        for i in range(len(board)):
            for j in range(len(board)):
                if board[j][i] == word[0]:
                    if dfs([(i, j)], word[1:], (i, j)):
                        return True
        return False


        