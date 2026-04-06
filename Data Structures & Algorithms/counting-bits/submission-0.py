class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        for i in range(n+1):
            numOnes = 0
            for j in range(32):
                if i & (j<<1):
                    numOnes+=1
            res.append(numOnes)
        return res


        