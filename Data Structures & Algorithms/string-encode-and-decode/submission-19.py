class Solution:
    #we can use the format: #intSizeOfStr
    def encode(self, strs: List[str]) -> str:
        ret = ''
        for i in strs:
            ret +=  str(len(i)) + '#' + i
       # print(ret)
        return ret
    def decode(self, s: str) -> List[str]:
        ret = []
        i = 0
        def findWord(currS):
            i = 0
            size = ''
            while currS[i] != '#':
                size += currS[i]
                i += 1
          #  print(i, currS[i:i+int(size)],currS[i+int(size):])
            return currS[i+1:i+1+int(size)], currS[i+1+int(size):]

        while s:
            x, s = findWord(s)
           # print(x, s)
            ret.append(x)



        return ret