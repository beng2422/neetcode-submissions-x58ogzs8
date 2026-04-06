class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        def search(x, y, word, used):
            if len(word)==0:
                return True
            if board[x][y]==word[0]:
                if len(word) == 1: 
                    return True
                used2 = used | {(x, y)}
                if x+1<len(board)   and (x+1, y) not in used and search(x+1, y, word[1:], used2):
                    return True
                if x-1>=0  and (x-1, y) not in used and search(x-1, y, word[1:], used2):
                    return True
                if  y+1<len(board[0]) and (x, y+1) not in used and search(x, y+1, word[1:], used2):
                    return True
                if  y-1>=0 and (x, y-1) not in used and search(x, y-1, word[1:], used2):
                    return True
                return False
            else:
                return False


        ret = []
        for word in words:
            for i in range(len(board)):
                for j in range(len(board[0])):


                    if search(i, j, word, set()):
                        ret.append(word)

        return ret