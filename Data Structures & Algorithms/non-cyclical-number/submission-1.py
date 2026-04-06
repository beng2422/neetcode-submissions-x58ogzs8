class Solution:
    def isHappy(self, n: int) -> bool:
        
        res = []
        while n!=1:
            sumVal = 0
            for char in str(n):
                sumVal+=int(char)**2
            if sumVal == 1:
                return True
            if sumVal in res:
                return False
            res.append(sumVal)
            n=sumVal
        return True