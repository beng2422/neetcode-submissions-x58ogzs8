class Solution:
    # do something like 5#HELLO
    def encode(self, strs: List[str]) -> str:
        encoding = ''
        for i in strs:
            encoding = encoding + len(i) + '#' + i
        return encoding



    def decode(self, s: str) -> List[str]:
        decoding = []
        for i in s:
            
            decoding.append(s[2:2+i])
            s = s[:2+i]
        return decoding