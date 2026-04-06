class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        

        def rec(cm, cn):
            if cm==1 or cn==1:
                return 1

            
            
            return rec(cm-1, cn) + rec(cm, cn-1)

        return rec(m, n)

            
        









