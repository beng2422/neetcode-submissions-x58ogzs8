class Solution:
    def reverseBits(self, n: int) -> int:
        res = []

        for i in range(32):
           # print(n>>i)
            print((n >> i)&1)
            res.append((n >> i)&1)
        res1 = 0
        res = res[::-1]
        print(res)
        for i in range(len(res)):
            if res[i]==1:
                res1 |= (1<<i)
        print(res1)
        return res1