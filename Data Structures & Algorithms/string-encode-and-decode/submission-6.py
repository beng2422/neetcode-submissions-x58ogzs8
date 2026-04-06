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
            
            print(s)
            decoding.append(s[2:2+int(s[0])])
            s = s[2+int(s[0]):]
        return decoding