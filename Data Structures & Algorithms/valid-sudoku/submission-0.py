class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Create multiple sets - a set of each 
        rows = {}
        cols = {}
        box = {}
        for i in range(len(board[0])):
            cols[i] = set()
            box[i] = set()
        

        for i in range(len(board)):
            rows[i] = set()
            for j in range(len(board[0])):

                if board[i][j] != '.' and board[i][j] in rows[i]:
                    return False
                elif board[i][j] != '.':
                    rows[i].add(board[i][j])
                
                if board[i][j] != '.' and board[i][j] in cols[j]:
                    return False
                elif  board[i][j] != '.':
                    cols[j].add(board[i][j])

                box_num = int(i/3) + 3*int(j/3)
                
                if board[i][j] != '.' and board[i][j] in box[box_num]:
                    print("HERE", i, j)
                    return False
                elif board[i][j] != '.':
                    box[box_num].add(board[i][j])
        return True



