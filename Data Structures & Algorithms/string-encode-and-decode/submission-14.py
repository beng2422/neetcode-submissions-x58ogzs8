class Solution:
    # do something like 5#HELLO
    def encode(self, strs: List[str]) -> str:
        encoding = ''
        for i in strs:
            encoding = encoding + str(len(i)) + '#' + str(i)
        print(encoding)
        return encoding



    def decode(self, s: str) -> List[str]:
        decoding = []
        while len(s)>0:
            
            num = s[0]
            s = s[1:]
            print('here', s[0])
            while s[0] != '#':
                num+=s[0]
                s = s[1:]
            decoding.append(s[1:2+int(num)])
            print(decoding)
            print('last one', s, 2+int(num))

            s = s[1+int(num):]
        return decoding