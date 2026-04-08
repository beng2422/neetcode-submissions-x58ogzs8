class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        maxJ = [False for _ in s]
        maxJ[0] = True
        i = 0

        while i < len(s):
            print(i, s[i], maxJ[i])
            if not maxJ[i]:
                i+=1
                continue
           #if s[i] == '0':
            for j in range(i+minJump, min(len(s), i+maxJump+1)):
                if s[j] == '0':
                    maxJ[j] = True
            i+=1

        return maxJ[len(s)-1]